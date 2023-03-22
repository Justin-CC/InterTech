from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from rango import models
from .models import User, Dish, Comment, Receive

"""
Homepage
"""


def index(request):
    # Get the info dictionary data from the session
    info_dict = request.session.get("info")
    # Render the template file and pass the info_dict data to the template file
    return render(request, 'index.html', {'info_dict': info_dict})


"""
Login
"""


def login(request):
    # Depending on the request method,
    if request.method == "GET":
        # Get the information from the session
        info_dict = request.session.get("info")
        # If no information is obtained, return to the login page
        if info_dict is None:
            return render(request, 'login.html', {'info_dict': info_dict})
        # If the information is obtained, return to the index page
        return render(request, 'index.html', {'info_dict': info_dict})
    # If the request method is POST, get the form information
    else:
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # Filter the user information in the database according to the username and password
        user_object = models.User.objects.filter(username=user, password=pwd).first()
        # If it exists, store the information in the session
        if user_object:
            request.session['info'] = {"id": user_object.userid, "name": user_object.username}
            return redirect('index')
        # If it does not exist, return an error message
        else:
            error = "The user name or password is incorrect"
            # If there is a comment in the form, assign the comment to the error
            comment = request.POST.get("comment")
            if comment:
                error = comment
            return render(request, 'login.html', {"error": error})


"""
Logout
"""


def logout(request):
    # clear the session
    request.session.clear()
    # redirect to the main page
    return redirect('index')


"""
Register
"""


def register(request):
    # Depending on the request method,
    if request.method == "GET":
        # Get the information from the session
        info_dict = request.session.get("info")
        # If no information is obtained, return to the register page
        if info_dict is None:
            return render(request, 'register.html', {'info_dict': info_dict})
        # If the information is obtained, return to the index page
        return render(request, 'index.html', {'info_dict': info_dict})

    else:
        # get data
        username = request.POST.get('register_username')
        phone_number = request.POST.get('register_phone_number')
        email = request.POST.get('register_email')
        pwd = request.POST.get('register_password')
        pwd_confirm = request.POST.get('register_confirm_password')

        # query user from database
        user_object = models.User.objects.filter(username=username).first()
        # if password not equal to confirm password
        if pwd != pwd_confirm:
            return render(request, 'register.html', {"error": "The password entered twice does not match"})
        # if the username already exists
        elif user_object:
            return render(request, 'register.html', {"error": "The username already exists"})
        # save user to database
        else:
            user = User(username=username, password=pwd, phone=phone_number, email=email)
            user.save()
            # return login page
            return render(request, 'login.html', {"error": "Registered successfully！"})


"""
View function to response user's request of main menu, and return the corresponding html file
"""


def menu(request):
    queryset = []
    # Get all dishes object
    for dish in Dish.objects.all():
        # Build dictionary to store dish information
        queryset.append({
            'dishid': dish.dishid,
            'dishname': dish.dishname,
            'type': dish.type,
            'price': dish.price,
            'dish_picture': dish.picture,
            'description': dish.description,
        })
    # Get user information
    info_dict = request.session.get("info")
    # Return menu html file, and pass user information in
    return render(request, "menu.html", {"data": queryset, 'info_dict': info_dict})


"""
This function is to show the details of the dish that user selects.
It will render a page with the dish's info, comments and a reminder.
"""


def menu_detail(request):
    # check if the request is GET or POST
    if request.method == "GET":
        # get the user's info from the session
        info_dict = request.session.get("info")
        # render the index page
        return render(request, "index.html", {'info_dict': info_dict})

    else:
        # get the user's info from the session
        info_dict = request.session.get("info")
        # get the dishid that user selects
        dishid = request.POST.get('dishid').replace('/', '')
        # get the dish object
        dish = Dish.objects.get(dishid=dishid)
        # get dish's name, type, price, description, and picture
        dishname = dish.dishname
        type = dish.type
        price = dish.price
        description = dish.description
        dish_picture = dish.picture

        # create a dictionary with dish's info
        data = {"dishid": dishid, "dishname": dishname, "type": type, "price": price, "description": description,
                "dish_picture": dish_picture, }

    # create a reminder empty string
    reminder = ""
    # get the comment from the request
    text = request.POST.get('text')
    # check if the comment is empty or not
    if text is not None and text.strip() != "":
        # change the reminder string
        reminder = "Thank you for your comment!"
        # get the dish object
        dish = Dish.objects.get(dishid=dishid)
        # get the user object
        user = User.objects.get(userid=info_dict['id'])
        # create a comment object
        comment = Comment(dish=dish, user=user, content=text)
        # save the comment
        comment.save()

    elif text is not None and text.strip() == "":
        # change the reminder string
        reminder = "Please enter the comment"

    # get all the comments from the dish
    tempcomments = Comment.objects.filter(dish__dishid=dishid)
    # create a comment list
    comments = []
    # go through all the comments
    for tempcomment in tempcomments:
        # create a dictionary for each comment
        comment_dict = {
            'dishid': tempcomment.dish.dishid,
            'userid': tempcomment.user.userid,
            'username': tempcomment.user.username,
            'comment': tempcomment.content,
        }
        # append the dictionary to the list
        comments.append(comment_dict)
    # render the menu_detail page
    return render(request, 'menu_detail.html',
                  {"data": data, "comment": comments, 'info_dict': info_dict, 'reminder': reminder})


"""
This view renders the aboutus.html template and passes the info_dict in the context.
"""


def aboutus(request):
    info_dict = request.session.get("info")
    return render(request, "aboutus.html", {'info_dict': info_dict})


"""
This function handles the contact us page of the website. 
When the user submit the contact us form, this function will save the received message and remind the user.
"""


def contactus(request):
    # get the information from session
    info_dict = request.session.get("info")
    if request.method == "GET":
        # render the contactus.html
        return render(request, "contactus.html", {'info_dict': info_dict})

    else:
        # get the required information from contactus.html
        name = request.POST.get('your_name')
        email = request.POST.get('your_email')
        title = request.POST.get('your_title')
        content = request.POST.get('your_content')

        if content is not None and content.strip():
            # save the received message
            receiveMessage = Receive(name=name, title=title, content=content, email=email)
            receiveMessage.save()
            # remind the user submit successfully
            return render(request, "contactus.html", {'info_dict': info_dict, "reminder": "Submit success！"})
        else:
            # remind the user to enter the comment
            return render(request, "contactus.html", {'info_dict': info_dict, "reminder": "Please enter the comment"})


"""
This view renders the faqs.html template and passes the info_dict in the context.
"""


def faqs(request):
    info_dict = request.session.get("info")
    return render(request, "faqs.html", {'info_dict': info_dict})
