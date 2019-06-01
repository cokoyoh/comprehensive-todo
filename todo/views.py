from django.db import transaction
from django.shortcuts import render, redirect
from django.utils import timezone
from .mails import Mailer

from .models import Todo


def index(request):
    if request.method == 'POST':
        task = request.POST['task']
        date = request.POST['date']
        created_at = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        todo = Todo(task=task, date=date, created_at=created_at, updated_at=created_at)
        todo.save()

        return redirect('/show')

    return render(request, 'index.html')


def show(request):
    todos = Todo.objects.all()
    return render(request, 'show.html', {'todos': todos})


@transaction.atomic
def mark_as_completed(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed_at = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    todo.save()

    data = {
        'task_name': todo.task,
        'date': todo.date
    }
    Mailer('Task Completed', ['john@example.com'], data).send()

    return redirect('/show')
