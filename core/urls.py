from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stay-tuned/<str:email>/', views.stay_tuned, name='stay_tuned'),
    path('discussion/', views.dicussions, name="discussions"),
    path('discussion/add-question/', views.add_question, name="add_question"),
    path('discussion/<int:question_id>/', views.question, name='question'),
    path('discussion/add-answer/<int:question_id>/', views.add_answer, name="add_answer"),
]