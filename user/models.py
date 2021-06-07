from django.db.models.fields import related
from assesment.models import questionPaper
from django.db import models
from django.contrib.auth.models import User

class questionPaperAttended(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    quest = models.ForeignKey(questionPaper, null=True, blank=True, on_delete=models.PROTECT)
    marksobtained = models.IntegerField()

    def marks(self):
        return self.marksobtained

    # def __str__(self):
    #     return 

class userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    questionPapersAttended = models.ManyToManyField(questionPaperAttended, related_name='attended', blank=True)

    def __str__(self):
        return str(self.user)