from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Task
from django.http import HttpResponse
# Create your views here.

class HomeView(View):
    def get(self,request):
        tasks=Task.objects.filter(is_completed=False).order_by('updated_at')
        com_task=Task.objects.filter(is_completed=True)
        return render(request,"home.html",{"tasks":tasks,"com_task":com_task})
    
def AddTaskView(request):
        task=request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')


def MarkDone(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')
    

def MarkUnDone(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')


def EditTask(request,pk):
    get_task=get_object_or_404(Task, pk=pk)
    if request.method=="POST":
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task
        } 
        return render(request,"edit_task.html",context)
    

def DeleteTask(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')