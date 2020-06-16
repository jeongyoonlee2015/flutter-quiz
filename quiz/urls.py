# quiz 폴더 안의 urls.py는 퀴즈 앱에 대한 url 관리

from django.urls import path, include
from .views import helloAPI, randomQuiz
urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", randomQuiz)
    
]