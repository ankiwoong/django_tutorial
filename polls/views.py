from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Question


# URLconf : 뷰를 호출하려면 이와 연결된 URL 이 있어야 하는데 이를 사용하기 위해 사용
# https://docs.djangoproject.com/ko/3.0/intro/tutorial01/#write-your-first-view


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # render(request, template_name, context=None, content_type=None, status=None, using=None)
    # request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며, context 사전형 객체를 세전째 선택적(optional) 인수
    # context로 표현된 템플릿의 HttpResponse 객체가 반환
    return render(request, 'polls/index.html', context)
# Leave the rest of the views (detail, results, vote) unchanged


def detail(request, question_id):
    # get_object_or_404(klass, *args, **kwargs)
    # Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다.
    # 만약 객체가 존재하지 않을 경우, Http404 예외가 발생합니다.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
