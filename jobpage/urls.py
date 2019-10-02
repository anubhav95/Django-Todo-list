from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add_to', views.add_to,name='add_to'),
    path('delete_todo/<int:todo_id>', views.delete_todo,name='delete_todo'),
]