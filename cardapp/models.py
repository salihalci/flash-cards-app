from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    questiondesc  = models.CharField(max_length=100)
    subject  = models.CharField(max_length=100,default='')
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questiondesc
