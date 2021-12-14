'''
author: Yiran Xu
'''
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add the urls.py in main urls file
    path('', include('api.urls')),
]
