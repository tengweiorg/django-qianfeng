from django.shortcuts import render
from django.http import HttpResponse

from user.models import *


#  视图函数Views
def index(request):
    pass
    # 返回相应response
    # return HttpResponse('Hello Django！')

    # 渲染模板render,渲染html
    return render(request, 'index.html')


# 视图函数2
def index2(request):
    return HttpResponse('Index2')


# 视图函数3
def get_users(request):
    # 模型操作；获取所有user
    users = UserModel.objects.all()
    return render(request, 'users.html', {'users': users})




