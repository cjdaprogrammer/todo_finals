from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage URL
    path('add/', views.add_task, name='add_task'),  # Add Task URL
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit Task URL
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete Task URL
    path('mark_done/<int:task_id>/', views.mark_done, name='mark_done'),  # Mark Done URL
]
