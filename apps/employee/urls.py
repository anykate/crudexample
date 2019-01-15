# https://www.javatpoint.com/django-crud-example

from django.urls import path
from . import views

app_name = 'employee_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:employee_id>/', views.edit, name='edit'),
    path('delete/<int:employee_id>/', views.delete, name='delete'),
]
