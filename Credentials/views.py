

from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        User=auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            print("Invalid credentials ")
            return redirect('login')
    return render(request,'login.html')

def register(request):
 
    
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        
        #user register and password checking

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                print("Username Taken")
                return redirect('register')
              
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                print("Email Taken")
                return redirect ('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
            print("user created")
            return redirect('login')
          
        else:
            #print("password not matching")
           
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')