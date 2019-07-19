from django.db import models

# Create your models here.

class AddressInfo(models.Model):
    """省市县地址信息"""
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    # 自关联，self也可以改成'AddressInfo'
    pid = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name="自关联")
    note = models.CharField(max_length=200, null=True, blank=True, verbose_name="说明")

    # 在2.7中是__unicode__(self)
    def __str__(self):
        return self.address

    # 通过内嵌类 class Meta 给model定义元数据
    class Meta:
        # 表名称
        db_table = 'address'
        # 模型对象返回的记录结果集按照哪个字段排序
        # ordering = ['pid']
        # 给模型起一个可读的名字
        verbose_name = '省市县地址信息'
        # 模型的复数形式
        verbose_name_plural = verbose_name
        # 是否虚拟类
        # abstract = True
        # permissions = (('定义好的权限', '权限说明'),)
        # 是否由django管理表
        # managed = False
        # 联合唯一
        unique_together = ('address', 'note')
        # app_label = 'courses'
        # 表空间，有些数据库有数据库表空间，比如Oracle
        # db_tablespace


class Teacher(models.Model):
    """讲师信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    introduction = models.TextField(default="这位同学很懒，木有签名的说~", verbose_name="简介")
    fans = models.PositiveIntegerField(default="0", verbose_name="粉丝数")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "讲师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

class Course(models.Model):
    """课程信息表"""
    title = models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name="课程名")
    # 课程关联讲师，讲师删除后，级联删除课程
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE,
                                verbose_name="课程讲师")
    type = models.CharField(choices=((1, "实战课"), (2, "免费课"), (0, "其他")), max_length=1, default=0, verbose_name="课程类型")
    price = models.PositiveSmallIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "课程信息表"
        get_latest_by = "created_at"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.get_type_display()}-{self.title}"

class Student(models.Model):
    """学生信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    # 学生关联课程，多对多关系
    # 会自动生成中间表courses_student_course
    course = models.ManyToManyField(Course, verbose_name="课程")
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.CharField(choices=((1, "男"), (2, "女"), (0, "保密")), max_length=1,
                              default=0, verbose_name="性别")
    study_time = models.PositiveIntegerField(default="0", verbose_name="学习时长(h)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "学生信息表"
        ordering = ['age']
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

class TeacherAssistant(models.Model):
    """助教信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    # 助教关联讲师，一对一关系
    teacher = models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name="讲师")
    hobby = models.CharField(max_length=100, null=True, blank=True, verbose_name="爱好")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "助教信息表"
        db_table = "courses_assistant"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname









