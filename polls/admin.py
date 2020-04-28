from django.contrib import admin
from .models import Question

# admin 페이지에 Question 출력
admin.site.register(Question)
