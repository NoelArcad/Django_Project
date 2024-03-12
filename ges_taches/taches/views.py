from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.template import loader
from .models import Task

def main(request):
    template = loader.get_template('main.html')  
    mytask = Task.objects.all().values()
    context = {'mytask': mytask}
    return render(request, 'main.html', context)
    
   
def add_task(request):
    mytask = Task.objects.all().values()
    template = loader.get_template('add_task.html')  
    context = {'mytask': mytask} 
    if request.method == 'POST':
        name_task = request.POST['name_task']
        des_task = request.POST['des_task']
        start_date_task = request.POST['start_date_task']
        start_time_task = request.POST['start_time_task']
        end_date_task = request.POST['end_date_task']
        end_time_task = request.POST['end_time_task'] 
        statut_task = request.POST['statut_task'] 
        new_task = Task(name_task=name_task, des_task=des_task, start_date_task=start_date_task, start_time_task=start_time_task, end_date_task=end_date_task, end_time_task=end_time_task, statut_task=statut_task)
        new_task.save()
        return redirect('main')
    return render(request, 'add_task.html', context)


def display_details_tasks(request, id):
    template = loader.get_template('display_details_tasks.html')
    mytask = Task.objects.filter(id=id)
    context = {'mytask': mytask}
    return render(request, 'display_details_tasks.html', context)
    
def modify_task(request, id):
    mytask = Task.objects.filter(id=id)
    template = loader.get_template('modify_task.html')  
    context = {'mytask': mytask} 
    if request.method == 'POST':
        name_task = request.POST['name_task']
        des_task = request.POST['des_task']
        start_date_task = request.POST['start_date_task']
        start_time_task = request.POST['start_time_task']
        end_date_task = request.POST['end_date_task']
        end_time_task = request.POST['end_time_task'] 
        statut_task = request.POST['statut_task'] 
        new_task = Task(id=id, name_task=name_task, des_task=des_task, start_date_task=start_date_task, start_time_task=start_time_task, end_date_task=end_date_task, end_time_task=end_time_task, statut_task=statut_task)
        new_task.save()
        return redirect('main')
    return render(request, 'modify_task.html', context)
    

def delete_task(request, id):
    mytask = Task.objects.filter(id=id)
    template = loader.get_template('delete_task.html')  
    context = {'mytask': mytask} 
    if request.method == 'POST':
        for x in mytask:
             
            x.delete()
        return redirect('main')
    return render(request, 'delete_task.html', context)