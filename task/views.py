from django.shortcuts import render, redirect
from .models import Task, Commends
from user.models import user_info
from .forms import Task_Form

def tasks(request, name):
    status = 404
    tasks_objects = Task.objects.none() # from avoid the problem (dont have tasks_object variable)
    user_object = user_info.objects.none() # from avoid the problem (dont have tasks_object variable)
    
    if user_info.objects.filter(name=name).exists():
        user_object = user_info.objects.get(name=name)
        username = user_object.name

    else:
        return redirect('/')

    if Task.objects.filter().exists():
        tasks_objects = Task.objects.all()
        status = 200
        
    if request.method == 'POST':
        form = Task_Form(request.POST)
        if form.is_valid():
            print(form)
            print('form')
            form.save()
            title = request.POST.get('title', 'null')
            description = title + ' was created by ' + username,
            Commends.objects.create(
                message = 'created alert',
                description = description,
                # task = task_object,
                user = user_object,
            )
            return redirect('tasks', username)
        else:
            print(form.errors)

    else:
        form = Task_Form()
    

    

    context = {
        'tasks':tasks_objects,
        'status':status,
        'user':user_object,

        'form':form,
    }

    return render(request, 'task/tasks.html', context)

def deleteTask(request, taskid, userid):
    
    task_object = Task.objects.none() # from avoid the problem (dont have tasks_object variable)
    user_object = user_info.objects.none() # from avoid the problem (dont have tasks_object variable)
    username = '' # from avoid the problem (dont have tasks_object variable)
    if Task.objects.filter(id=taskid).exists():    #if we have a task with this id from avoid the problem
        task_object = Task.objects.get(id=taskid)
        title = task_object.title
        task_object.delete()
        if user_info.objects.filter(id=userid).exists():
            user_object = user_info.objects.get(id=userid)
            username = user_object.name
            
            description = title + ' was deleted by ' + username,
            Commends.objects.create(
                message = 'deleted alert',
                description = description,
                # task = task_object,
                user = user_object,
            )
        

    
    return redirect('tasks', username)



def edittask(request, taskid, userid):
    
    task_object = Task.objects.none() # from avoid the problem (dont have tasks_object variable)
    user_object = user_info.objects.none() # from avoid the problem (dont have tasks_object variable)
    username = '' # from avoid the problem (dont have tasks_object variable)
    if Task.objects.filter(id=taskid).exists():    #if we have a task with this id from avoid the problem
        task_object = Task.objects.get(id=taskid)
        title = task_object.title
        
        if user_info.objects.filter(id=userid).exists():
            user_object = user_info.objects.get(id=userid)
            username = user_object.name

            if request.POST :
                #get input values
                title = request.POST.get('title', 'null')
                description = request.POST.get('description', 'null')
                priority = request.POST.get('priority', 'null')
                status = request.POST.get('status', 'null')
                print(priority)
                print(status)
                
                # edit_task is html btn name 
                if 'edit_task' in request.POST:
                    task_object.title = title
                    task_object.description = description
                    task_object.priority = priority
                    task_object.status = status
                    task_object.save()

                    return redirect ('tasks', username)

            
            description = title + ' was updated by ' + username,
            Commends.objects.create(
                message = 'updated alert',
                description = description,
                task = task_object,
                user = user_object,
            )
    
    context = {
        'task': task_object,
    }
    
    return render(request, 'task/edit_task.html', context)


