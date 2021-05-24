from django.http import request
from django.shortcuts import redirect, render
from todo.models import Task
from todo.forms import TaskForm
from django.contrib import messages

# Create your views here.
def index(request):
    task_list = Task.objects.order_by("-date")
    context_dict = {'tasks' : task_list}
    return render(request,'todo/index.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'todo/about.html',context_dict)

def add_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            task = form.save(commit=True)
            return index(request)  # direct user back to index page
            
        else:
            print(form.errors)
    
    context_dict = {'form' : form}
    return render(request,'todo/add_task.html',context_dict)

def remove_task(request):
    task_id = request.GET.get('DeleteButton')

    print('To be Deleted : ',task_id)
    item = Task.objects.get(title = task_id)
    print(item)
    item.delete()
    messages.info(request, "Item removed !!!")
    return index(request)