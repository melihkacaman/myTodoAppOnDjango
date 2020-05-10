from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from random import randint
from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()

    context = {
        'todo_list': todo_list,
        'form': form
    }
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(quest=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.isComplete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(isComplete__exact=True).delete()

    return redirect('index')

def rndQuest(request):
    rnd_list = []
    for i in range(10):
        rnd_list.append("Random Quest" + str(i))

    our_rnd = rnd_list[randint(0,9)]

    new_todo = Todo(quest=our_rnd)
    new_todo.save()

    return redirect('index')
