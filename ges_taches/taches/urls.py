from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_task/', views.add_task, name='add_task'), 
    path('display_tasks/<int:id>/', views.display_details_tasks, name='display_details_tasks'),
    path('modify_task/<int:id>/', views.modify_task, name='modify_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    
]

