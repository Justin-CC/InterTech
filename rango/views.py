from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    return render(request, "index.html")


#     category_list = Category.objects.order_by('-likes')[:5]
#     page_list = Page.objects.order_by('-views')[:5]
#
#     context_dict ={}
#     context_dict['boldmessage'] ='Crunchy, creamy, cookie, candy, cupcake!'
#     context_dict['categories'] = category_list
#     context_dict['pages'] = page_list
#     return render(request, 'rango/index.html',context=context_dict)

# 
# def about(request):
#     context_dict ={'boldmessage': 'This page is replaced by Justin!'}
#     return render(request, 'rango/about.html',context=context_dict)
#     #return HttpResponse("Restauraunt introduction")
# 
# def show_category(request, category_name_slug):
#     context_dict = {}
#     try:
#         category = Category.objects.get(slug=category_name_slug)
# 
#         pages = Page.objects.filter(category=category)
# 
#         context_dict['pages'] = pages
# 
#         context_dict['category'] = category
#     except Category.DoesNotExist:
# 
#         context_dict['category'] = None
#         context_dict['pages'] = None
# 
#     return render(request, 'rango/category.html', context=context_dict)
# 
# 
# def add_category(request):
#     form = CategoryForm()
# 
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
# 
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('/rango/')
#         else:
#             print(form.errors)
# 
#     return render(request, 'rango/add_category.html', {'form': form})
# 
# 
# def add_page(request, category_name_slug):
#     try:
#         category = Category.objects.get(slug=category_name_slug)
#     except:
#         category = None
# 
#     # You cannot add a page to a Category that does not exist... DM
#     if category is None:
#         return redirect('/rango/')
# 
#     form = PageForm()
# 
#     if request.method == 'POST':
#         form = PageForm(request.POST)
# 
#         if form.is_valid():
#             if category:
#                 page = form.save(commit=False)
#                 page.category = category
#                 page.views = 0
#                 page.save()
# 
#                 return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
#         else:
#             print(form.errors)  # This could be better done; for the purposes of TwD, this is fine. DM.
# 
#     context_dict = {'form': form, 'category': category}
#     return render(request, 'rango/add_page.html', context=context_dict)

def login(request):
    # 判断到底是POST请求还是GET请求
    if request.method == "GET":
        return render(request, 'login.html')
    else:

        # 去请求中获取数据，再进行校验
        username = request.POST.get('user')
        password = request.POST.get('pwd')

        # 去数据库中校验，用户名和密码的合法性

        # 成功，跳转到index http://127.0.0.1:8000/index/    /index/
        # return redirect('/index')

        # 不成功，再次让用户看到login页面 -> 用户名或密码错误
        # return request('/login.html', {"error": "用户名或密码错误"})

        if username == 'root' and password == '123':
            return redirect('index')
        else:
            return render(request, 'login.html', {"error": "The user name or password is incorrect"})

def register(request):
    return render(request, "register.html")
def menu(request):
    return render(request, "menu.html")
def menu_detail(request):
    return render(request, "menu_detail.html")
def aboutus(request):
    return render(request, "aboutus.html")
def contactus(request):
    return render(request, "contactus.html")
def faqs(request):
    return render(request, "faqs.html")
