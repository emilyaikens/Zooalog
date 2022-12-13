# import path from zooalog/urls.py
# the path function is used to define each route
# CBV(class based view) ListView, DetailView, CreateView, DeleteView and UpdateView
# CBVs require a int:pk, rather than int:test_id
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('enclosures/', views.enclosure_index, name='index'),
    path('enclosures/<int:enclosure_id>/', views.enclosure_detail, name='detail'),
    path('enclosures/create/', views.EnclosureCreate.as_view(), name='enclosure_create'),
    path('enclosures/<int:pk>/update/', views.EnclosureUpdate.as_view(), name="enclosure_update"),
    path('enclosures/<int:pk>/delete/', views.EnclosureDelete.as_view(), name="enclosure_delete"), 
    path('enclosures/<int:enclosure_id>/add_animal/', views.add_sub, name='add_sub'),
    path('accounts/signup', views.signup, name='signup'),
    ]
    