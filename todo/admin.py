from django.contrib import admin
from todo.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'deadline')

admin.site.register(Task, TaskAdmin)
# Register your models here.
