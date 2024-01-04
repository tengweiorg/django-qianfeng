from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from App.models import *

# 首页
def index(request):
    return render(request, 'index.html')


# 用户列表
def user_list(request):
    # 获取所有用户数据
    users = UserModel.objects.all()
    return render(request, 'user_list.html', {'users': users})


# 用户详情
def user_detail(request, uid):
    # print('uid:', uid)
    user = UserModel.objects.get(pk=uid)  # pk: primary key 主键
    return render(request, 'user_detail.html', {'user': user})


# 多个参数
def user_ab_view(request, a, b):
    return HttpResponse(f'a:{a} - b:{b}')

# 要和路由中的参数名一致，名字对应赋值
def user_ba_view(request, b, a):
    return HttpResponse(f'a:{a} - b:{b}')


# 重定向
def my_redirect(request):
    # return redirect('https://www.ifeng.com')
    # return redirect('/user/userlist/')
    # return redirect('/user/userdetail/2/')

    # 反向解析
    # reverse('App:userdetail', args=(1,)) => 'userdetail/1/'
    # 带命名空间的写法
    # return redirect(reverse('App:userdetail', args=(1,)))  # 位置参数传参
    return redirect(reverse('App:userdetail', kwargs={'uid': 2}))  # 关键字传参
    # 不带命名空间
    # return redirect(reverse('userdetail', args=(1,)))  # 位置参数传参


