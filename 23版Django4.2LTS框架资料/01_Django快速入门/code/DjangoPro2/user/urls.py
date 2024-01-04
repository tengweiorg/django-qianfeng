from django.urls import path
from user.views import *

# 子路由
urlpatterns = [
    # url路由写法: django v1.x,v2.x
    # url(r'^index/', index),

    # v2.x, v3.x, v4.x
    path('index/', index, name='index'),
    path('index2/', index2, name='index2'),

    path('users/', get_users, name='users'),

]

