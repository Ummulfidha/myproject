from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def gymclubb(request):
    return render(request,'index.html')

def admin_loginn(request):
    if request.method == 'POST':
        a = adminloginform(request.POST)
        if a.is_valid():
            email = a.cleaned_data['email']
            pwd = a.cleaned_data['pwd']
            if email == 'admingymm@gmail.com' and pwd == 'admingymm':
                return redirect('admin_home')
            else:
                return HttpResponse("please enter valid email and password")
    else:
        return render(request,'admin_login.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def add_trainer(request):
    if request.method == 'POST':
        print("IN POST")
        a = addtrainerform(request.POST)
        print("HELLO")
        print(a)
        if a.is_valid():
            print("FORM VALID")
            tname = a.cleaned_data['tname']
            tage = a.cleaned_data['tage']
            tphone = a.cleaned_data['tphone']
            temail = a.cleaned_data['temail']
            tadm = a.cleaned_data['tadm']
            b = addtrainermodel(tname=tname, tage=tage, tphone=tphone, temail=temail, tadm=tadm)
            b.save()
            return redirect(view_trainer)
        else:
            return HttpResponse("failed")
    else:
        return render(request, 'add_trainer.html')


def view_trainer(request):
    obj = addtrainermodel.objects.all()
    print(obj)
    return render(request, 'view_trainer.html', {'obj':obj})

def view_client(request):
    return render(request, 'view_client.html')

def gym_classs(request):
    return render(request, 'gym_class.html')

def edit_delete(request):
    return render(request, 'edit_delete.html')

def edit_delete_client(request):
    return render(request, 'edit_delete_client.html')

def admin_logout(request):
    try:
        del request.session['user']
    except:
        return redirect('admin_login')
    return redirect('admin_login')

#trainer

def trainer_home(request):
    return render(request, 'trainer_home.html')


def trainer_login(request):
    if request.method == 'POST':
        a = trainerloginform(request.POST)
        if a.is_valid():
            email = a.cleaned_data['email']
            pwd = a.cleaned_data['pwd']
            if email == 'trainer@gmail.com' and pwd == 'trainergym':
                return redirect('trainer_home')
            else:
                return HttpResponse("please enter valid email and password")
    else:
        return render(request,'trainer_login.html')


