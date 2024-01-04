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
from django.urls import path

from App.views import *

urlpatterns = [

    path('add/', add_person),  # 添加数据
    path('del/', del_person),  # 删除数据
    path('update/', update_person),  # 修改数据
    path('get/', get_person),  # 查询数据

    # 分页
    path('paginate/<int:page>/', paginate, name='paginate'),
    path('paginate2/<int:page>/', paginate2, name='paginate2'),

    path('admin/', admin.site.urls),
]
