from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False, verbose_name='类型名称')

    class Meta:
        db_table = 'teacher'
        verbose_name = '授课老师'
        verbose_name_plural = verbose_name

    # 调整列表页面的显示   中文显示
    def __str__(self):
        return self.name
class Classes(models.Model):
    cla_name = models.CharField(max_length=32, unique=True, verbose_name='班级名称')

    teacher = models.ManyToManyField(to=Teacher, verbose_name='授课老师')

    class Meta:
        db_table = 'classes'
        verbose_name = '班级名称'
        verbose_name_plural = verbose_name

    # 调整列表页面的显示   中文显示
    def __str__(self):
        return self.cla_name


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=32, unique=True)
    classes = models.ForeignKey(to=Classes, on_delete=models.CASCADE, verbose_name='班级')
    class Meta:
        db_table = 'student'
        verbose_name = '学生姓名'
        verbose_name_plural = verbose_name

    # 调整列表页面的显示   中文显示
    def __str__(self):
        return self.name