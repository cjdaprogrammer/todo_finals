from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    tasks = Task.objects.all() 
    return render(request, 'todo/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        if task_name:
            Task.objects.create(task_name=task_name) 
    return redirect('home') 

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        if task_name: 
            task.task_name = task_name
            task.save() 
        else:
            print("Task name cannot be empty!")
            return redirect('home') 
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home') 

def mark_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = True  # Assuming there's an `is_done` field in the Task model
    task.save()
    return redirect('home')  # Redirect to task list after marking the task as done
