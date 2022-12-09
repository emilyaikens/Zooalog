# import path from zooalog/urls.py
# the path function is used to define each route
# CBV(class based view) ListView, DetailView, CreateView, DeleteView and UpdateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('test/', views.test_index, name='index'),
    path('test/<int:test_id>/', views.test_detail, name='detail'),
    path('test/create/', views.TestCreate.as_view(), name='test_create')
]