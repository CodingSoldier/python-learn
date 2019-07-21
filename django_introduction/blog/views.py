from django.shortcuts import render
from django.http import HttpResponse

from blog import models
from blog.models import Article
from django.core.paginator import Paginator


def hello_world(request):
    return HttpResponse("Hello World")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date

    str = '标题：%s，摘要：%s，内容：%s, id %s, date: %s ' \
        % (title, brief_content, content, article_id, publish_date)

    return HttpResponse(str)


def get_index_page(request):
    page = request.GET.get('page')
    page = int(page) if page else 1

    all_article = Article.objects.all()

    # 排序，publish_date倒序
    top10_article_list = Article.objects.order_by('-publish_date')[:2]

    # 分页
    paginator = Paginator(all_article, 2)
    page_num = paginator.num_pages
    print('page num:', page_num)
    page_article_list = paginator.page(page)
    print("数据", page_article_list)

    # 返回模板与变量
    return render(request, 'blog/index.html', {
        'article_list': page_article_list,
        'top10_article_list': top10_article_list
    })

def get_detail_page(request, article_id):
    all_article = Article.objects.all()
    curr_article = None
    for article in all_article:
        if article.article_id == article_id:
            curr_article = article
            break

    return render(request, 'blog/detail.html',{
        'curr_article': curr_article,
        'section_list': curr_article.content
    })
























