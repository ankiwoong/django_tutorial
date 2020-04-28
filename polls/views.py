from django.http import HttpResponse


'''
1. 첫 번째 뷰 작성하기
- URLconf : 뷰를 호출하려면 이와 연결된 URL 이 있어야 하는데 이를 사용하기 위해 사용
https://docs.djangoproject.com/ko/3.0/intro/tutorial01/#write-your-first-view
'''


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
