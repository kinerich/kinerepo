from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


@login_required(login_url='users:login')
def todolist(request):
    if request.method == 'POST':
        inputs = forms.AddTask(request.POST)
        if inputs.is_valid():
            new_task = inputs.save(commit=False)
            new_task.save()
            return redirect('lists:todolist')
    else:
        inputs = forms.AddTask()
    task = Task.objects.all().order_by('-date')
    return render(request, 'lists_of_todo/todolist.html',
    {'task': task, 'inputs': inputs})
