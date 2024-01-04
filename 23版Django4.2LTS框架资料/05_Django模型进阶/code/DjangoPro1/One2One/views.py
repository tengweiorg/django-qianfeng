from django.shortcuts import render, HttpResponse
from One2One.models import *

# 一对一
# 增删改：和一对多是类似的

# 查询
def get(request):
    # 查找某用户的身份证信息
    user = User.objects.get(pk=1)
    print(user.idcard)  # 对象
    print(user.idcard.idcard_num, user.idcard.address)

    # 查找身份证对应的用户
    idcard = IDCard.objects.get(pk=1)
    print(idcard.user)  # 对象
    print(idcard.user.name, idcard.user.age, idcard.user.sex)

    return HttpResponse('查询成功!')




