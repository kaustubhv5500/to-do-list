from django.shortcuts import render
from todo.models import Task
from todo.forms import TaskForm

# Create your views here.
def index(request):
    task_list = Task.objects.order_by("-date")
    context_dict = {'tasks' : task_list}
    return render(request,'todo/index.html', context_dict)

def add_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=True)
            return index(request)  #direct user back to index page
        else:
            print(form.errors)
    
    context_dict = {'form' : form}
    return render(request,'todo/add_task.html',context_dict)

def remove_task(request,task_id):
    pass