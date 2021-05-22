from todo.models import Task
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from todo.models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=75, help_text="Enter the Title of Task")
    description = forms.CharField( widget=forms.Textarea)
    date = DateField(widget=forms.HiddenInput(), initial=timezone.now())
    deadline = DateField(widget=AdminDateWidget)
    
    class Meta:
        model = Task
        fields = ('title', 'description','deadline')
