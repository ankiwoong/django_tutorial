import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# pub_date를 가진 Question` 인스턴스를 생성하는 메소드를 가진 django.test.TestCase 하위 클래스를 생성


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
