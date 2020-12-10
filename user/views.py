import hashlib

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.urls import reverse

from user.models import User


def register(request):
    if request.method == 'GET':
        return render(request, "user/register.html")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        phone = request.POST.get('phone')
        if username and password and repassword:
            if password == repassword:
                # 数据库添加用户
                user = User()
                user.username = username
                user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if phone:
                    user.phone = phone
                print(user)
                user.save()
                return HttpResponse('用户注册成功')
            else:
                return render(request, "user/register.html", {"msg": "密码不一致"})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        flag = check_password(password, user.password)
        if flag:
            request.session["username"] = username
            return redirect(reverse("user:show"))
        else:
            return render(request, "user/login.html", {"msg": "用户名或者密码错误！"})
    else:
        return render(request, "user/login.html", {"msg": "用户名或者密码不能为空！"})
    return render(request, "user/login.html")


def show(request):
    users = User.objects.all()
    return render(request, "user/show.html", {"users": users})


def delete(request):
    id = request.GET.get('id')
    user = User.objects.get(pk=id)
    if user:
        # 删除
        # user.delete()
        user.is_delete = 1
        user.save()
        return redirect(reverse("user:show"))
    else:
        return HttpResponse('用户删除失败')


def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        is_delete = request.POST.get('is_delete')
        # 更新方式1
        # user = User.objects.get(pk=id)
        # user.username = username
        # user.phone = phone
        # user.is_delete = is_delete
        # user.save()
        # 方式2
        # 前端如果选中checkbox name就会得到字符串on，否则就是个空值
        if is_delete == "on":
            is_delete = True
        else:
            is_delete = False
        result = User.objects.filter(id=id).update(username=username, phone=phone, is_delete=is_delete)
        return redirect(reverse("user:show"))
    else:
        id = request.GET.get('id')
        user = User.objects.get(pk=id)
        if user:
            return render(request, "user/update.html", {"user": user})
        else:
            redirect(reverse("user:show"))


def user_login(request):
    return render(request, "user/user_login.html")


def user_register(request):
    return render(request, "user/user_register.html")


def logout(request):
    request.session.flush()
    return render(request, "user/user_login.html")


def is_login(request):
    username = request.session.get("username")
    user = User.objects.filter(username=username).first()
    if user:
        return JsonResponse({"username": username, "status": 200})
    else:
        return JsonResponse({"status": 456})
