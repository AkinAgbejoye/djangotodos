from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpRequest, HttpResponse
import datetime
from  .models import Todo
def list_todos_items(request):
    content = {'todo_list':Todo.objects.all()}
    return render(request, 'todos/todos.html',content)

def insert_todos_items(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def delete_todos_items(request,todo_id):
    todo_item_delete =  Todo.objects.get(id=todo_id)
    todo_item_delete.delete()
    return redirect('/todos/list/')
 