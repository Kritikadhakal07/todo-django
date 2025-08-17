from django.urls import path
from . import views

urlpatterns=[
    path('addTask/',views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),
    path('mark_as_undo/<int:pk>/',views.mark_as_undo, name='mark_as_undo'),
    path('edit_task/<int:pk>/',views.editTask, name='editTask'),
    path('delete_task/<int:pk>/',views.deleteTask, name='deleteTask'),
]