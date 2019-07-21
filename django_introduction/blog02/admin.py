from django.contrib import admin

# Register your models here.
from blog02.models import Article02, Tags, Category

admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Article02)