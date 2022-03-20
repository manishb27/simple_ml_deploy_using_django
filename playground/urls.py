# mapping the urls to view functions 
from django.urls import path 
from . import views



## urlCONF
urlpatterns = [
    path('', views.home , name = "home"),
    path('result/', views.result, name = "result")
]
