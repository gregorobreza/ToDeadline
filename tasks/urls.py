from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.tasks_list, name='task_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_done_tasks/', views.deleteDoneTasks, name='delete_done_tasks'),
    path('done_task/<str:pk>/', views.doneTask, name="done_task"),
    path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
    path('<slug:category_slug>/', views.tasks_list, name='task_list_by_category'),
    path('delete_category/<str:pk>/', views.delete_category, name='delete_category'),
    
]