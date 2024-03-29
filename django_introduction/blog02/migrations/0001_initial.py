# Generated by Django 2.2.3 on 2019-07-19 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
        ),
        migrations.CreateModel(
            name='Article02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('intro', models.TextField(blank=True, max_length=200, verbose_name='摘要')),
                ('body', models.TextField(blank=True, max_length=200, verbose_name='内容')),
                ('create_time', models.DateTimeField(verbose_name='发布时间')),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='blog02.Category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, to='blog02.Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
