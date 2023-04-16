"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.main,name='main'),
    path('about/',views.about,name='about'),
    path('home/',views.home,name='home'),
    path('index',views.index,name='index'),
    path('display/',views.display,name='display'),
    path('add',views.add,name='Add'),
    path('remove',views.remove,name='Remove'),
    path('remove/<int:i_id>',views.remove,name='Remove'),
    path('filter',views.filter,name='Filter'),  
   # path('<int:id>/',views.update,name="updatedata"),  
    path('Login/',views.Login,name='Login'),
    path('contact/',views.contact,name='contact'),
]   
