from django.http import request
from django.shortcuts import redirect, render
from todo.models import Task
from todo.forms import TaskForm
from django.contrib import messages
from calendar import HTMLCalendar
import calendar

# Create your views here.
def index(request):
    task_list = Task.objects.order_by("deadline")
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
            return index(request) # direct user back to index page
            
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

def calendar_view(request):
    task_list = Task.objects.order_by("deadline")
    current_year = task_list[0].deadline.year
    current_month = task_list[0].deadline.month
    cal = HTMLCalendar().formatmonth(current_year,current_month)


    month_str = task_list[0].deadline.strftime("%B") + ' ' + str(current_year)
    cal = cal.replace(month_str,'Fill',1)
    cal = cal.replace("0","2",1)
    cal = cal.replace("0","42",1)
    cal = cal.replace("0","99",1)

    # current_month = return_current_month(request) 

    for i in range(len(task_list)):
        # if task_list[i].deadline.month == current_month:
        date = str(task_list[i].deadline.date()).split('-')[2]
        replace_str = date + '<br/><strong>' + task_list[i].title + '</strong>'
        cal = cal.replace(date,replace_str,1)

    cal = cal.replace('Fill',month_str,1)

    context_dict = {'tasks' : task_list, 'cal':cal}

    return render(request, 'todo/calendar_view.html', context_dict)


#  Finish Function Definition
def return_current_month(request):
    task_list = Task.objects.order_by("deadline")
    current_month = task_list[0].deadline.month

    query_dict = dict(request.POST)
    
    prev_month = query_dict['PreviousMonth']
    print('Query Return Value : ',prev_month)
    print(query_dict.keys())

    return current_month

