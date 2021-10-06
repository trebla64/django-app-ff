from django.urls import path

from . import views

urlpatterns = [
    path('client/add', views.addClient, name='addClient'),
    path('', views.index, name='index'),
]
