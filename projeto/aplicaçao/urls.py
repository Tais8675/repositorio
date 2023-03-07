from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.index, name="index"),
    path("barbie", views.index, name="index")
 ]
