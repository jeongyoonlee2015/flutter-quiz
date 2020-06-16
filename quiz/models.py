from django.db import models

# 모델 만들기
# 시리얼 라이저 만들기: 장고 모델 데이터를 JSON 타입으로 바꿔주는(직렬화) 코드

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()