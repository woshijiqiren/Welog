"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .Controllers import hello
from django.views.generic import TemplateView, RedirectView
from django.conf.urls import url
from model import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello.hello),
    url(r'^welog/', TemplateView.as_view(template_name="index.html")),
    url(r'^api/seleteuser/', views.selete_users),
    url(r'^api/login/', views.login),
    url(r'^api/adduser/', views.adduser),
    url(r'^api/deleteuser/', views.deleteuser),
    url(r'^api/listtable/', views.listtable),
    url(r'^api/upload/', views.uploadfile),
    url(r'^api/listvideo',views.listvoide),
    url(r'^api/addvideo',views.addvoide),
    url(r'^api/listfriend',views.listfriend),
]
