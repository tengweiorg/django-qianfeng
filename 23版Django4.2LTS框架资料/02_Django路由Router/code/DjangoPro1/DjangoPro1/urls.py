"""
URL configuration for DjangoPro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App.views import *

urlpatterns = [

    #  1. 直接使用根路由
    # path('user/', index),

    # 2. 使用子路由: 使用include
    # path('user/', include('App.urls')),

    # 3. 使用子路由: 使用include,命名空间namespace
    #  如果用了命名空间，后面的反向解析（包括视图函数和模板中）都要使用命名空间
    path('user/', include(('App.urls', 'App'), namespace='App')),

    path('admin/', admin.site.urls),
]
