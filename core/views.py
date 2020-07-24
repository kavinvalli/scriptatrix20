from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.views.generic.list import ListView
import random
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/authentication/login')
def dicussions(request):
    all_questions = Question.objects.all().order_by('-pub_date')
    recommended_questions = random.sample(list(all_questions), 2)
    context = {
        'questions': all_questions,
        'recommended_questions':recommended_questions
    }
    return render(request, 'core/html/discussions/discussions.html', context)

def add_question(request):
    posted_by_user = request.user
    text = request.POST.get('question')
    Question.objects.create(
        posted_by_user=posted_by_user,
        text=text
    )
    url = '/discussion/'
    return redirect(url)

def question(request, question_id):
    all_questions = Question.objects.all().order_by('-pub_date')
    question = Question.objects.get(id=question_id)
    recommended_questions = random.sample(list(all_questions), 2)
    context = {
        'question': question,
        'recommended_questions':recommended_questions
    }
    return render(request, 'core/html/discussions/question.html', context)

def add_answer(request, question_id):
    posted_by_user = request.user
    text = request.POST.get("answer")
    question = Question.objects.get(id=question_id)
    Answer.objects.create(
        posted_by_user = posted_by_user,
        question=question,
        text=text
    )
    url = '/discussion/' + str(question_id) + '/'
    return redirect(url)