from django.shortcuts import render,redirect
from .models import Todomd
from django.shortcuts import get_object_or_404

def todo_list(request):
    todos=Todomd.objects.all()
    return render(request,'all_todo.html',{'todos':todos})

def  todo_create(request):
    if request.method=='POST':
        task=request.POST["todoname"] 
        Todomd.objects.create(task=task)
        return redirect('todo_list')    

    
    return render(request,'create_todo.html')


def todo_delete(request,id):
    todo= get_object_or_404(Todomd,pk=id)
    todo.delete()
    return redirect('todo_list')

def todo_edit(request,id):
    todow=get_object_or_404(Todomd,pk=id)
    if request.method == "POST":
        task=request.POST["todoname"]
        todow.task=task
        todow.save()
        return redirect('todo_list')

        

    
    return render(request,'edit_todo.html',{'todo':todow})

def todo_complete(request,id):
    todo=get_object_or_404(Todomd,pk=id)
    todo.completed=not todo.completed
    todo.save()
    return redirect('todo_list')










     



    



# Create your views here.
