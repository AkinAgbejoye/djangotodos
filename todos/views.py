from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def list_todos_items(request):
    x =1 
    y =2
    now = datetime.datetime.now()
    html = "<html><body>It is now %s </body></html>" % now
    return render(request,'todos/todos.html',{'name':'Mosh'})
    # return HttpResponse(html)