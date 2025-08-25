from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    #hna mdari nst3mlo get mais hna edna li fihom false o true hna habina y3tina li rahom false
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request, 'home.html' , context)