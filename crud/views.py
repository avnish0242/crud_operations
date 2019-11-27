from django.shortcuts import render, redirect
from crud.forms import TaskForm
from crud.models import Task


# Create your views here.


def tsk(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                form.save()
                return redirect('/show')
    else:
        form = TaskForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    tasks = Task.objects.all()
    return render(request, "show.html", {'tasks': tasks})


def edit(request, id):
    task = Task.objects.get(taskid=id)
    return render(request, 'edit.html', {'task': task})


def update(request, id):
    task = Task.objects.get(taskid=id)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': task})


def destroy(request, id):
    task = Task.objects.get(taskid=id)
    task.delete()
    return redirect("/show")
