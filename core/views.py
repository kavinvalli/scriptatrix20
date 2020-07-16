from django.shortcuts import render
from . models import *
from django.http import JsonResponse

def index(request):
    if request.method == "GET":
        return render(request, "core/html/index.html")

def stay_tuned(request, email):
    data = dict()
    if request.method == "POST":
        data = {
            'is_taken': StayTuned.objects.filter(email__iexact=email).exists()
        }
        if data['is_taken']:
            data['error_message'] = 'You have already joined our Vibrant Community'
        else:
            data['error_message'] = 'Your email ' + email + ' has been added to our Subscribers list'
            StayTuned.objects.create(
                email=email,
            )
        return JsonResponse(data)