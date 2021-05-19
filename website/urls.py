"""LYPIN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from website import views

urlpatterns = [
    path('',views.index, name='home'),
    path('index.html',views.index, name='home'),
    path('cbse.html',views.cbse, name='cbse'),
    path('icse.html',views.icse, name='icse'),
    path('cbse-class10.html',views.cbseclass10, name='cbseclass10'),
    path('icse-class10.html',views.icseclass10, name='icseclass10'),
    path('cbse-class12.html',views.cbseclass12, name='cbseclass12'),
    path('icse-class12.html',views.icseclass12, name='icseclass12'),
    path('pu.html', views.pu, name= 'pu'),
    path('ba.html', views.ba, name= 'ba'),
    path('ba1.html', views.ba1, name= 'ba1'),
    path('pu.html', views.pu, name= 'pu'),
    path('pu.html', views.pu, name= 'pu'), 
]


