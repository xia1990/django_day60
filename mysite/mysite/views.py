#!/usr/bin/python3
#_*_ coding:utf-8 _*_
from django.shortcuts import HttpResponse,render,redirect

def yimi(request):
    return HttpResponse("hello yimi!")

def xiaohei(request):
    return HttpResponse("hello xiaohei!")

def login(request):
    error_message=""
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email == "admin@163.com" and password == "123456":
            return redirect("http://luffycity.com")
        else:
            # return HttpResponse("登录失败！")
            error_message="邮箱或密码错误！"
    return render(request, "login.html",{"error":error_message})

def baobao(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    if email=="admin@163.com" and password=="1223456":
        return HttpResponse("登录成功!")
    else:
        return HttpResponse("登录失败！")

