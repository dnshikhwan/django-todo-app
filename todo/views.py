from django.shortcuts import render, redirect, get_object_or_404
from django.http import request, HttpResponse
from .models import TodoList
from .forms import TodoForm, UpdateTodoForm
from django.contrib.auth.decorators import login_required


def todo_list(request):
    try:
        todolist = TodoList.objects.filter(user=request.user)
        context = {'todos': todolist}
        return render(request, 'index.html', context=context)
    except:
        return render(request, 'index.html')


@login_required(login_url='login')
def add_todo(request):
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form_user = form.save(commit=False)
            form_user.user = request.user
            form_user.save()
            return redirect('todo-list')

    context = {'form': form}
    return render(request, 'add-todo.html', context=context)


@login_required(login_url='login')
def todo_delete(request):
    if request.POST.get('action') == 'post':
        todo_id = int(request.POST.get('todo_id'))
        todo_list = get_object_or_404(TodoList, user=request.user, id=todo_id)
        todo_list.delete()
        return redirect('todo-list')


@login_required(login_url='login')
def todo_update(request, title):
    todo = get_object_or_404(TodoList, title=title)

    if request.method == 'POST':
        update_form = UpdateTodoForm(request.POST, instance=todo)

        if update_form.is_valid():
            update_form.save()
            return redirect('todo-list')

    update_form = UpdateTodoForm(instance=todo)
    context = {'update_form': update_form}
    return render(request, 'edit-todo.html', context=context)
