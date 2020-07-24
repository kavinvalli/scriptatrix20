from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    posted_by_user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, related_name='question_posted_by_user')
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    # sub_text = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    posted_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='answer_posted_by_user')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_question')
    text = models.CharField(max_length=10000)
    
    def __str__(self):
        return self.text

class StayTuned(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email