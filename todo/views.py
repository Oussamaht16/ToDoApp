from encodings.punycode import T
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render , redirect
from .models import Task
# Create your views here.

def addtask(request):
    taskr = request.POST['task'] #hadi 'task'hia nafsha li rahi dakhal name dakhal input dakhal html
    Task.objects.create(task=taskr  )# lokhrin madarnahomch psq wahad rahi par defaut o zoj li b9aw auto generated
    #print(request.POST)
    return redirect('home')



def mark_as_done(request, pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task , pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
      context = {
          'get_task':get_task,
                }  
    return render(request, 'edit_task.html' , context)


def delete_task(request, id):
    task = get_object_or_404(Task , id=id )
    task.delete()
    return redirect('home')
