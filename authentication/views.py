from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            url = '/discussion/'
            return redirect(url)
        else:
            return render(request, 'authentication/html/login.html')
    elif request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            url = "/discussion/"
            return redirect(url)
            # return HttpResponse('logged in')
        else:
            return render(request, "authentication/html/login.html", {"message": "Invalid credentials."})

def registration_view(request):
    if request.method == "GET":
        return render(request, 'authentication/html/register.html')
    elif request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        try:
            User.objects.get(username=email_id)
            return render(request, "authentication/html/register.html", {"message": "User with username exists"})
        except:
            if "@" not in email_id:
                return render(request, "authentication/html/register.html", {"message": "Invalid Email Id"})
            else:
                if len(password) < 6:
                    return render(request, "authentication/html/register.html", {"message": "Password needs to be atleast 8 characters long"})
                else:
                    user = User.objects.create_user(email_id, email_id, password)
                    user.first_name=first_name
                    user.last_name=last_name
                    user.save()
                    auth_login(request, user)
                    url = "/discussion/"
                    return redirect(url)
                    # return redirect('/authentication/login/')

def logout_view(request):
    auth_logout(request)
    url = '/'
    return redirect(url)