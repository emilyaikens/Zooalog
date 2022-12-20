# import path from zooalog/urls.py
# the path function is used to define each route
# CBV(class based view) ListView, DetailView, CreateView, DeleteView and UpdateView
# CBVs require a int:pk, rather than int:test_id
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),

    path('enclosures/', views.enclosure_index, name='index'),
    path('enclosures/<int:enclosure_id>/', views.enclosure_detail, name='detail'),
    path('enclosures/create/', views.EnclosureCreate.as_view(), name='enclosure_create'),
    path('enclosures/<int:pk>/update/', views.EnclosureUpdate.as_view(), name='enclosure_update'),
    path('enclosures/<int:pk>/delete/', views.EnclosureDelete.as_view(), name='enclosure_delete'), 

    path('animals/<int:enclosure_id>/add_animal', views.add_animal, name='add_animal'),
    path('animals/<int:enclosure_id>/create_animal/', views.create_animal, name='create_animal'),
    path('animals/<int:animal_id>/update/', views.update_animal, name='update_animal'),
    path('animals/<int:pk>/delete', views.AnimalDelete.as_view(), name='delete_animal'),

    path('parameters/<int:enclosure_id>/create_parameter/', views.create_parameter, name='create_parameter'),
    path('parameters/<int:parameter_id>/update/', views.update_parameter, name='update_parameter'),
    path('parameters/<int:pk>/delete', views.ParameterDelete.as_view(), name='delete_parameter'),
    path('parameters/info', views.parameter_info, name='parameter_info'),

    path('diets/<int:enclosure_id>/create_diet', views.create_diet, name='create_diet'),
    path('diets/<int:diet_id>/update/', views.update_diet, name='update_diet'),
    path('diets/<int:pk>/delete', views.DietDelete.as_view(), name='delete_diet'),

    path('logs/<int:enclosure_id>/parameters', views.log_parameter, name='log_parameter'),
    path('logs/<int:enclosure_id>/parameter_logs', views.parameter_logs, name='parameter_logs'),
    path('logs/<int:enclosure_id>/diets', views.log_diet, name='log_diet'),
    path('logs/<int:enclosure_id>/diet_logs', views.diet_logs, name='diet_logs'),

    path('accounts/signup', views.signup, name='signup'),
    ]
    