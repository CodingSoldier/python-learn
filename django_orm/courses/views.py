from django.http import HttpResponse
from django.db.models import Sum, Avg, F, Q
from django.shortcuts import render

# Create your views here.
# 导入models必须加上.
from .models import Teacher, Student, TeacherAssistant, Course



def orm(request):

    # # 查询所有
    # teachers = Teacher.objects.all()
    # print(teachers)
    #
    # # 只返回一条结果，多条会报错
    # teacher2 = Teacher.objects.get(nickname='Jack')
    # print(teacher2)
    #
    # # 可以是多条记录
    # teacher3 = Teacher.objects.filter(fans__gt=500)
    # for t in teacher3:
    #     print(f"讲师姓名{t.nickname}--粉丝数{t.fans}")
    #
    # # 字段匹配，大小写敏感
    # teacher4 = Teacher.objects.filter(fans__in=[666, 1231])
    # print(f"teacher4--{teacher4}")
    #
    # teacher5 = Teacher.objects.filter(nickname__icontains='A')
    # print(f"teacher5--{teacher5}")
    #
    # # 切片
    # print(f"切片--{Teacher.objects.all()[:1]}")
    # # 排序
    # print(f"排序--{Teacher.objects.all().order_by('-fans')}")
    #
    # # 链式查询
    # print(f"链式查询--{Teacher.objects.filter(fans__gte=500).order_by('nickname')}")
    #
    # # 查看原生sql
    # print(f"原生sql：{str(Teacher.objects.filter(fans__gte=500).order_by('nickname').query)}")
    #
    #
    # """QuerySet API"""
    # print(f"排除--{Student.objects.all().exclude(nickname='A同学')}")
    # print(f"反向排序，Student元数据中必须有ordering--{Student.objects.all().exclude(nickname='A同学').reverse()}")
    #
    # # 字段别名
    # s3 = Student.objects.all().extra(select={'name': 'nickname'})
    # print("字段别名:")
    # for s in s3:
    #     print(s.name)
    #
    # print(f"返回字典数据：{TeacherAssistant.objects.values('nickname', 'hobby')}")
    # print(f"返回数组元组：{TeacherAssistant.objects.values_list('nickname', 'hobby')}")
    # print(f"返回数组：{TeacherAssistant.objects.values_list('nickname', flat=True)}")
    #
    # print(f"根据日期查询：{Course.objects.dates('created_at', 'year', order='DESC')}")
    # print(f"根据日期查询：{Course.objects.datetimes('created_at', 'year', order='DESC')}")
    #
    # p_240 = Course.objects.filter(price__gte=240)
    # p_260 = Course.objects.filter(price__lte=260)
    # # union报错了
    # # print(p_240.union(p_260))

    # # select_related一对一、多对一查询
    # courses = Course.objects.all().select_related('teacher')
    # for c in courses:
    #     print(f"{c.title}--{c.teacher.nickname}--{c.teacher.fans}")

    # prefetch_related一对多，多对一
    # students = Student.objects.filter(age__lt=13).prefetch_related('course')
    # for s in students:
    #     print(s.course.all())

    # print(f"求和：{Course.objects.values('teacher').annotate(vol=Sum('volume'))}")
    # print(f"求平均值：{Course.objects.values('teacher').annotate(pri=Avg('price'))}")

    # print(Course.objects.first())
    # print(Course.objects.last())
    # print(Course.objects.earliest())
    # print(Course.objects.latest())
    # print(Course.objects.in_bulk(['Python系列教程4', 'Golang系列教程1']))
    #
    # # 2.创建对象 create(), bulk_create(), update_or_create() 创建，批量创建，创建或更新
    #
    # # 3.更新对象 update(), update_or_create() 更新，更新或创建
    # Course.objects.filter(title='Java系列教程2').update(price=300)
    #
    # # 删除对象delete()，使用filter过滤
    # Course.objects.filter(title='test').delete()
    #
    # # 数量
    # print(Course.objects.count())


    # F对象操作字段数据
    # price全部减11
    Course.objects.update(price=F('price') - 11)
    # volume小于price*10
    print(Course.objects.filter(volume__lte=F('price') * 10))

    #Q对象结合AND、OR、NOT实现复杂查询
    print(Course.objects.filter(Q(title__icontains='java') & Q(volume__gte=5000)))
    print(Course.objects.filter(Q(title__icontains='golang') | Q(volume__lte=1000)))



    return HttpResponse("ok")












