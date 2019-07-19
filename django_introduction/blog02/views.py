from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog02.models import Article02


def hello(request):
    return HttpResponse("Hello, world")

def index(request):
    blog_index = Article02.objects.all().order_by('-id')
    context = {
        'blog_index': blog_index,
    }
    return render(request, 'index.html', context)

def method01(request):

    # print("path: ", request.path)
    # print("fullpath: ", request.get_full_path())
    # print("method: ", request.method)

    # param = request.GET
    # print("get请求参数：", param)
    # print("获取请求参数值name：", param.get('name'))



    return render(request, 'index.html')






