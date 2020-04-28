from django.db import models


class Question(models.Model):
    # CharField : 문자(character) 필드 / max_length : 필드의 최대 길이(문자)
    question_text = models.CharField(max_length=200)
    # DateTimeField : 날짜와 시간(datetime)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
