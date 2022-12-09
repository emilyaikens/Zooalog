# import path from zooalog/urls.py
# the path function is used to define each route
# CBV(class based view) ListView, DetailView, CreateView, DeleteView and UpdateView
# CBVs require a int:pk, rather than int:test_id
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('test/', views.test_index, name='index'),
    path('test/<int:test_id>/', views.test_detail, name='detail'),
    path('test/create/', views.TestCreate.as_view(), name='test_create'),
    path('test/<int:pk>/update/', views.TestUpdate.as_view(), name="test_update"),
    path('test/<int:pk>/delete/', views.TestDelete.as_view(), name="test_delete"), 
    path('test/<init:test_id>/add_sub/', views.add_sub, name='add_sub'),
]