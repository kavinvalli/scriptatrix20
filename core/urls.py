from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stay-tuned/<str:email>/', views.stay_tuned, name='stay_tuned'),
]