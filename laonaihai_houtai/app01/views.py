from django.shortcuts import render, redirect

# Create your views here.
from app01 import models


def login(request):
    models.Administrator.objects.create(
        username='he',
        password='123'
    )
    print(request.method)
    message = ''
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = models.Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            req = redirect('/index')
            req.set_cookie('username', user)

            return req
        else:
            message = "用户名或密码错误"
    return render(request, 'login.html', {'msg': message})


def index(req):
    # if req.COOKIES
    username = req.COOKIES.get('username')
    if username:
        return render(req, 'index.html', {'username': username})
    else:
        return redirect('/login')
