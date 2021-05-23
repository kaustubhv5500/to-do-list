from django.conf.urls import url
from todo import views

app_name = "todo"

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^about',views.about, name='about'),
    url(r"^add_task/$",views.add_task,name = "add_task"),
]
    