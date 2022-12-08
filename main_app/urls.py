# import path from zooalog/urls.py
# the path function is used to define each route
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
]