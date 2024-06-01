from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from ETL import views


app_name = 'ETL'

urlpatterns = [
    # home page
    path('', views.dashboard, name='dashboard'),

    # file upload urls
    path('upload/', views.upload_page, name='upload_page'),
    # path('file_upload/', views.file_upload, name='fileupload'),

    path('processed/', views.processed, name='processed'),
    path('master-view/', views.master, name='master-view'),
    path('structure-cv/<int:id>', views.structure, name='structure-cv'),
    
]
    