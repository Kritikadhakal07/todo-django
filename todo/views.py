from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from todo.models import Task
from django.shortcuts import get_object_or_404

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    #first task is the name of the field in the model
    #second task is the value of the field
    #like we take the value user enters in the field and put it in the model
    return redirect('home')

def mark_as_done(request,pk):
    # task = Task.objects.get(pk=pk)
    task = get_object_or_404(Task,pk=pk)
    #first pk is the name of the field in the model
    #second pk is the dynamic primary key we are passing from url
    #example Task.objects.get(pk=1)
    #like we take the value user clicks in the field and put it in the model
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undo(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')
    # return HttpResponse(pk)

def editTask(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['editTask']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task
        }
     
    return render(request,'editTask.html',context)



def deleteTask(request,pk):
    delete_task = get_object_or_404(Task,pk=pk)
    delete_task.delete()
    return redirect('home')