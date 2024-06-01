from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from Lin_Lou import views


app_name = 'Lin_Lou'

urlpatterns = [
    # home page
    
    
    # login stuff
    path('', views.login_page, name='login'),
    path('login/', views.firebase_login, name='firebase_login'),
    path('logout/', views.firebase_logout, name='logout'),

    
]