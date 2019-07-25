from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog01 import models


def orm(request):

    # 增加一篇文章
    models.Article.objects.create(title='增加标题一', category=3, body='增加内容一', user=1)
    return HttpResponse("ok")