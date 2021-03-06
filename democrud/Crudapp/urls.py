from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.employee_create),
    path('read', views.employee_read),
    path('update', views.employee_update),
    path('delete', views.employee_delete),
    path('list', views.employee_list)
]
