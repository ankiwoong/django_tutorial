from django.http import HttpResponse

# URLconf : 뷰를 호출하려면 이와 연결된 URL 이 있어야 하는데 이를 사용하기 위해 사용
# https://docs.djangoproject.com/ko/3.0/intro/tutorial01/#write-your-first-view


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
