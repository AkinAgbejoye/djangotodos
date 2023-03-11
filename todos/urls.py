from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.list_todos_items),
    path('insert_todos/', views.insert_todos_items, name="insert_todos_items"),
    path('delete_todos/<todo_id>/', views.delete_todos_items, name="delete_todos_items")
]