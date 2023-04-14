from django.shortcuts import render, redirect
from .models import Todo
from .forms import UpdateTodoForm
from datetime import datetime


# Create your views here.

def tasks(request):
    todos = Todo.objects.all()
    now = datetime.now()

    context = {
        'todos': todos,
        'year': now.strftime("%y"),
    }
    return render(request, 'tasks/tasks.html', context)


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'tasks/detail.html', context)


def create(request):
    name = request.GET.get('q')
    body = request.GET.get('t')
    if name is not None:
        Todo.objects.create(title=name, body=body)
        return redirect('tasks')

    context = {
        'query': name,
    }
    return render(request, 'tasks/create.html', context)


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()

    return redirect('tasks')


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = UpdateTodoForm(request.POST, instance=todo)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.filter(id=todo_id).update(title=cd['title'], body=cd['body'])
            form.save()
            return redirect('detail', todo_id)
    else:
        form = UpdateTodoForm(instance=todo)

    context = {
        'form': form,
    }

    return render(request, 'tasks/update.html', context)


def finished(request, todo_id):
    Todo.objects.filter(id=todo_id).update(status=0)

    return redirect('tasks')
