from django.urls import path
from restuarent import views

urlpatterns= [
    path("menu",views.fun1),
    path("item",views.fun2),
    path("add",views.fun3)
]