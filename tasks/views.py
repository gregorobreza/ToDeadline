from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Task

from .forms import CategoryForm, TaskForm

from django.contrib import messages
from datetime import datetime

# Create your views here.
def tasks_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    tasks = Task.objects.all()
    choices = [ i[0] for i in Task._meta.get_field('level').choices]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        tasks = tasks.filter(category=category)

    category_form = CategoryForm()
    task_form = TaskForm()
    return render(request, 'tasks/tasks/list.html', {'category':category, 'categories':categories, 'tasks':tasks, 'choices':choices, 'category_form':category_form, 'task_form':task_form})


def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
        else:
            messages.error(request, 'This category already exists. Please add another one.')


        return redirect('/')


def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()

    return redirect('/')

def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
        else:
            messages.error(request, 'Deadline cannot be in the past! Please add task again.')

        return redirect('/')


def doneTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.complete = True
        item.finished = datetime.now()
        item.save()

    return redirect('/')

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()

    return redirect('/')

def deleteDoneTasks(request):
    items = Task.objects.filter(complete=True)
    if request.method == "POST":
        items.delete()

    return redirect('/')