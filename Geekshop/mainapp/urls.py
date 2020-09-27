# from django.contrib import admin
# from django.conf import settings
from django.urls import path

import mainapp.views as mainapp

app_nama = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<category_pk>/', mainapp.products, name='category'),
]
