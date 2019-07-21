from django.contrib import admin

# Register your models here.

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 设置在列表中的字段
    list_display = ('article_id', 'title', 'publish_date')

    # 每页显示多少条记录，默认是100条
    list_per_page = 10

    # 排序字段，减号表示降序
    ordering = ('-publish_date', )

    # 列表中可编辑的字段
    # list_editable = ['title']