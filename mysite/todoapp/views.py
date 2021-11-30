from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo.html', page)

def remove(request, id):
    item_list = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        item_list.delete()
        messages.info(request, "item removed !!!")
    return redirect('todo')