from django.shortcuts import render
from django.http import HttpResponse


def login_view(request):
    if request.method == "GET":
        return HttpResponse("Login View")

def registration_view(request):
    if request.method == "GET":
        return HttpResponse("Registration View")

def logout_view(request):
    if request.method == "GET":
        return HttpResponse("Logout View")