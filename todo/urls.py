from django.conf.urls import url
from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^about',views.about, name='about'),
    url(r"^add_task/$",views.add_task,name = "add_task"),
    url(r'^deleteURL/(?P<task_id>[0-9]+)/$', views.remove_task, name='deleteURL'),
    path('deleteURL',views.remove_task),
    url(r'^modifyURL/(?P<task_id>[0-9]+)/$', views.modify_task, name='modifyURL'),
    path('modifyURL',views.modify_task),
    url(r"^modify_task/$",views.modify_task,name = "modify_task"),
    path('currentMonth',views.return_current_month),
    url(r'^calendarView/currentMonth$', views.return_current_month, name='currentMonth'),
    url(r'calendarView/$',views.calendar_view, name="calendar_view"),
]
    