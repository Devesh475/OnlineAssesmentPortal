from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class question(models.Model):
    Question = models.CharField(max_length=500)
    A = models.CharField(max_length=200)
    B = models.CharField(max_length=200)
    C = models.CharField(max_length=200)
    D = models.CharField(max_length=200)
    marks = models.IntegerField(default=1)
    answer = models.CharField(max_length=1)

    def __str__(self):
        return self.Question or str(self.id)

class questionPaper(models.Model):
    users = models.ManyToManyField(User, related_name='user', blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    questionList = models.ManyToManyField(question, blank=True, related_name='questionsList')
    submittedby = models.ManyToManyField(User, related_name='submitted', blank=True)
    examOverStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.title or "No Title"