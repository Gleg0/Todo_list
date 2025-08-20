from django.shortcuts import render, redirect, get_object_or_404
from todo_list.models import Task, Tag
from todo_list.forms import TaskForm, TagForm


def index(request):
    tasks = Task.objects.all()
    return render(request, "todo_list/index.html", {"tasks": tasks})


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("index")


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TaskForm()
    return render(
        request,
        "todo_list/form.html",
        {
            "form": form,
            "title": "Add Task"
        }
    )


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        "todo_list/form.html",
        {
            "form": form,
            "title": "Update Task"}
    )


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("index")
    return render(
        request,
        "todo_list/delete.html",
        {
            "object": task,
            "cancel_url": "index"
        }
    )


def tag_list(request):
    tags = Tag.objects.all()
    return render(
        request,
        "todo_list/tag_list.html",
        {
            "tags": tags
        }
    )


def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag-list")
    else:
        form = TagForm()
    return render(
        request,
        "todo_list/form.html",
        {
            "form": form,
            "title": "Add Tag"
        }
    )


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("tag-list")
    else:
        form = TagForm(instance=tag)
    return render(
        request,
        "todo_list/form.html",
        {
            "form": form,
            "title": "Update Tag"
        }
    )


def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("tag-list")
    return render(
        request,
        "todo_list/delete.html",
        {
            "object": tag,
            "cancel_url": "tag-list"
        }
    )
