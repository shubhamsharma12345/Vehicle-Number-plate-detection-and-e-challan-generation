from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings


from main import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('uploadimage', views.uploadimage, name='uploadimage'),
    path('user', views.user, name='user'),
    path('userval', views.userval, name='userval'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)