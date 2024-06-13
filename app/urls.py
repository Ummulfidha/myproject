"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns = [
    path('',views.gymclubb,name='gymclub'),
    #admin
    path('admin_login', views.admin_loginn, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('add_trainer', views.add_trainer, name='add_trainer'),
    path('add_trainer', views.add_trainer, name='add_trainer'),
    path('gym_class', views.gym_classs, name='gym_class'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('edit_delete', views.edit_delete, name='edit_delete'),
    path('view_trainer', views.view_trainer, name='view_trainer'),
    path('view_client', views.view_client, name='view_client'),
    #path('admin_logoutt', views.admin_logoutt, name='admin_loqoutt'),

    path('trainer_home', views.trainer_home, name='trainer_home'),
    path('trainer_login', views.trainer_login, name='trainer_login'),
    path('edit_delete_client', views.edit_delete_client, name='edit_delete_client'),

]
