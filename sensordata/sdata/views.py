from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import *
from django.http import HttpResponse,HttpResponseRedirect

# view for signup page
def signup(request):
    if (request.method == 'POST'):
        name = request.POST['uname1']
        email = request.POST['uemail1']
        pswd = request.POST['upswd1']
        d = User.objects.all()
        u = []
        for k in d:
            u.append(k.username)
        if name in u:
            return HttpResponse('Username Already Exist Please Login')
        users = User.objects.create_user(name, email, pswd)
        users.save()
        return HttpResponseRedirect('login')
    return render(request, 'signup.html')

def login1(request):
    if (request.method == 'POST'):
        name = request.POST['uname2']
        pswd = request.POST['upswd2']
        usernow = authenticate(request,username = name,password = pswd)
        if usernow is not None:
            login(request,usernow)
            print('logged In')
            return HttpResponseRedirect('monitor')
        else:
            print('Not Logged In')
            return HttpResponseRedirect('login')
    return render(request,'login.html')

# view for login page
def logout1(request):
    if(request.method == 'POST'):
        return logout(request)

# Saving data in Database that is from a Iot server through request
def cdata(request):
    if 'ok' in request.GET:
        gas = str(request.GET.get('gas'))
        temp = str(request.GET.get('temp'))
        fire = str(request.GET.get('fire'))
        moi = str(request.GET.get('moi'))
        light = str(request.GET.get('light'))
        values = labdata(gas=gas,temp=temp,fire=fire,mois=moi,light=light)
        values.save()
        print(gas,temp,fire,moi,light)
        print(type(gas))
        return HttpResponse('Data Saved')
    return HttpResponseRedirect('monitor') # Redirect to monitor page after saved data

#Rendering the data in a template
@login_required(login_url='login') #Decorator for proper authentication
def monitor(request):
    data = labdata.objects.all()
    return render(request,'table.html',{'data':data})

# signout
def signout1(request):
    logout(request)
    return HttpResponseRedirect('login')
