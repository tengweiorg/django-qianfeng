
from django.contrib import admin
from django.urls import path

from One2Many import views as one2many_view
from Many2Many import views as many2many_view
from One2One import views as one2one_view

urlpatterns = [

    # one2many
    path('one2many/adduser/', one2many_view.add_user),
    path('one2many/deluser/', one2many_view.del_user),
    path('one2many/updateuser/', one2many_view.update_user),
    path('one2many/getuser/', one2many_view.get_user),

    # many2many
    path('many2many/add/', many2many_view.add),
    path('many2many/delete/', many2many_view.delete),
    path('many2many/get/', many2many_view.get_user_movie),

    # one2one
    path('one2one/get/', one2one_view.get),

    path('admin/', admin.site.urls),
]
