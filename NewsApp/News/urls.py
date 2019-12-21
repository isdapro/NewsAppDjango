from django.contrib import admin
from django.urls import include, path
from . import views
from django.views.generic.base import TemplateView

urlpatterns=[
    path('',views.home, name='home'),
    path('search',views.search, name='search'),
    path('myloc',views.myloc, name='myloc'),
    path('addtask', views.addtask, name='addtask'),
    path('removetask',views.removetask, name='removetask'),
    path('mytasks',views.mytasks, name='mytasks'),

]
