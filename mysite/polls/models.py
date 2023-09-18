





import datetime

from django.db import models
from django.utils import timezone

# admin import
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    siuu = models.CharField(max_length=200, default='siu')
    testi = models.CharField(max_length=200, default='')

    MOI = "moi_1"
    HEY = "hey_1"
    HI = "hi_1"
    # choices 
    choices = [(MOI, "moi"),( HEY,"hey"), (HI,"hi")]

    greating = models.CharField(
        max_length=5,
        choices=choices,
        default="moi",
    )

    # makes a button to sort list
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



