from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    posted_by_user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, related_name='question_posted_by_user')
    text = models.CharField(max_length=1000)
    sub_text = models.CharField(max_length=1000, null=True, blank=True)

class Answer(models.Model):
    posted_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='answer_posted_by_user')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_question')
    text = models.CharField(max_length=10000)