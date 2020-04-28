import datetime
from django.db import models
# from django.utils import timezone : Django의 시간대 관련 유틸리티
from django.utils import timezone

# 각 변수는 모델의 데이터베이스 필드


# Question : 질문과 날짜
class Question(models.Model):
    # CharField : 문자(character) 필드 / max_length(필수인수) : 필드의 최대 길이(문자)
    question_text = models.CharField(max_length=200)
    # DateTimeField : 날짜와 시간(datetime)
    pub_date = models.DateTimeField('date published')
    # [Vscode] E1101:Class has no ‘objects’ member repair
    objects = models.Manager()

    # 호출할 때마다 호출 / Django 가 자동으로 생성하는 관리 사이트 에서도 객체의 표현이 사용
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Choice : 선택의 텍스트와 투표 집계 / 각 선택은 질문과 관련
class Choice(models.Model):
    # ForeignKey : 관계설정(다-대-일(many-to-one), 다-대-다(many-to-many), 일-대-일(one-to-one) 과 같은 모든 일반 데이터베이스의 관계들를 지원)
    # 각각의 Choice 가 하나의 Question 에 관계
    # on_delete : ForeignKeyField가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법
    # CASCADE : ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # CharField : 문자(character) 필드 / max_length(필수인수) : 필드의 최대 길이(문자)
    choice_text = models.CharField(max_length=200)
    # IntegerField : 32 비트 정수형 필드 / default(선택적 인수)
    votes = models.IntegerField(default=0)
    # [Vscode] E1101:Class has no ‘objects’ member repair
    objects = models.Manager()

    # 호출할 때마다 호출 / Django 가 자동으로 생성하는 관리 사이트 에서도 객체의 표현이 사용
    def __str__(self):
        return self.choice_text
