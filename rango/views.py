from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from rango import models
from .models import User, Dish, Comment, Contactus


def index(request):
    info_dict = request.session.get("info")
    return render(request, 'index.html', {'info_dict': info_dict})


def login(request):
    # 判断到底是POST请求还是GET请求
    if request.method == "GET":
        info_dict = request.session.get("info")
        if info_dict is None:
            return render(request, 'login.html', {'info_dict': info_dict})

        return render(request, 'index.html', {'info_dict': info_dict})

    else:

        # 去请求中获取数据，再进行校验
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        # 去数据库中校验，用户名和密码的合法性

        user_object = models.User.objects.filter(username=user, password=pwd).first()

        # 成功，跳转到index
        if user_object:
            request.session['info'] = {"id": user_object.userid, "name": user_object.username}
            return redirect('index')

        # 不成功，再次让用户看到login页面 -> 用户名或密码错误
        # return request('/login.html', {"error": "用户名或密码错误"})

        else:
            error = "The user name or password is incorrect"
            comment = request.POST.get("comment")
            if comment:
                error = comment
            return render(request, 'login.html', {"error": error})


def logout(request):
    request.session.clear()
    return redirect('index')


def register(request):
    if request.method == "GET":
        info_dict = request.session.get("info")
        if info_dict is None:
            return render(request, 'register.html', {'info_dict': info_dict})

        return render(request, 'index.html', {'info_dict': info_dict})

    else:
        username = request.POST.get('register_username')
        phone_number = request.POST.get('register_phone_number')
        email = request.POST.get('register_email')
        pwd = request.POST.get('register_password')
        pwd_confirm = request.POST.get('register_confirm_password')

        user_object = models.User.objects.filter(username=username).first()
        if pwd != pwd_confirm:
            return render(request, 'register.html', {"error": "The password entered twice does not match"})
        elif user_object:
            return render(request, 'register.html', {"error": "The username already exists"})
        else:
            user = User(username=username, password=pwd, phone=phone_number, email=email)

            user.save()
            return render(request, 'login.html', {"error": "Registered successfully！"})


def menu(request):
    # 这里要拿到全部的dish信息
    queryset = []
    for dish in Dish.objects.all():
        queryset.append({
            'dishid': dish.dishid,
            'dishname': dish.dishname,
            'type': dish.type,
            'price': dish.price,
            'dish_picture': dish.picture,
            'description': dish.description,

        })

    info_dict = request.session.get("info")
    return render(request, "menu.html", {"data": queryset, 'info_dict': info_dict})


def menu_detail(request):
    if request.method == "GET":
        info_dict = request.session.get("info")
        return render(request, "index.html", {'info_dict': info_dict})

    else:
        # 判断用户是否已登陆
        info_dict = request.session.get("info")

        dishid = request.POST.get('dishid').replace('/', '')
        # dishname = request.POST.get('dishname').replace('/', '')
        # type = request.POST.get('type').replace('/', '')
        # price = request.POST.get('price').replace('/', '')
        # description = request.POST.get('description').replace('/', '')
        # dish_picture = request.POST.get('dish_picture')

        dish = Dish.objects.get(dishid=dishid)
        dishname = dish.dishname
        type = dish.type
        price = dish.price
        description = dish.description
        dish_picture = dish.picture

        data = {"dishid": dishid, "dishname": dishname, "type": type, "price": price, "description": description,
                "dish_picture": dish_picture, }

    reminder = ""
    text = request.POST.get('text')
    if text is not None and text.strip() != "":
        reminder = "Thank you for your comment!"
        print(text)
        print(dishid)
        print(info_dict['id'])
        # print(info_dict['name'])

        # 在这里把text存入comment数据库,content里存text，dish_id里存dishid，user_id里存info_dict['id']，就都是我上面print里面的，测过了没问题
        dish = Dish.objects.get(dishid=dishid)
        user = User.objects.get(userid=info_dict['id'])
        comment = Comment(dish=dish, user=user, content=text)
        comment.save()

    elif text is not None and text.strip() == "":
        reminder = "Please enter the comment"

    # 根据dishid匹配到dish所对应的comment，里面应该有对这个菜品进行评价的用户名id（主键），用户名，用户的评论
    tempcomments = Comment.objects.filter(dish__dishid=dishid)
    comments = []
    for tempcomment in tempcomments:
        comment_dict = {
            'dishid': tempcomment.dish.dishid,
            'userid': tempcomment.user.userid,
            'username': tempcomment.user.username,
            'comment': tempcomment.content,
        }
        comments.append(comment_dict)

    return render(request, 'menu_detail.html',
                  {"data": data, "comment": comments, 'info_dict': info_dict, 'reminder': reminder})


def aboutus(request):
    info_dict = request.session.get("info")
    return render(request, "aboutus.html", {'info_dict': info_dict})


def contactus(request):
    info_dict = request.session.get("info")
    if request.method == "GET":
        return render(request, "contactus.html", {'info_dict': info_dict})

    else:
        name = request.POST.get('your_name')
        email = request.POST.get('your_email')
        title = request.POST.get('your_title')
        content = request.POST.get('your_content')

        if content is not None and content.strip():
            contactus = Contactus(name=name, title=title, content=content, email=email)
            contactus.save()
            return render(request, "contactus.html", {'info_dict': info_dict, "reminder": "Submit success！"})
        else:
            return render(request, "contactus.html", {'info_dict': info_dict, "reminder": "Please enter the comment"})


def faqs(request):
    info_dict = request.session.get("info")
    return render(request, "faqs.html", {'info_dict': info_dict})
