'''
author: Yiran Xu
'''
from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('', views.getTeams, name='TeamMembers'),
    # add page
    path('add/',views.createMember, name='add'),
    # edit page
    path('edit/<str:pk>/',views.editMember, name='edit'),
]
