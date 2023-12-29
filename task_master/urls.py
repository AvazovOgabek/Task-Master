from django.urls import path
from . import views


urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('done-task/<int:task_id>/', views.done_task, name='done_task'),
    
]