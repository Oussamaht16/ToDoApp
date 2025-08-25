from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Task
# Create your views here.

def addtask(request):
    taskr = request.POST['task'] #hadi 'task'hia nafsha li rahi dakhal name dakhal input dakhal html
    Task.objects.create(task=taskr  )# lokhrin madarnahomch psq wahad rahi par defaut o zoj li b9aw auto generated
    return redirect('home')