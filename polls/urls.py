from django.urls import path
from . import views

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    # route : URL 패턴을 가진 문자열
    # view :  HttpRequest 객체를 첫번째 인수로 하고, 경로로 부터 '캡처된' 값을 키워드 인수로하여 특정한 view 함수를 호출
    # kwargs : 임의의 키워드 인수들은 목표한 view 에 사전형으로 전달
    # name : 템플릿을 포함한 Django 어디에서나 명확하게 참조
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
