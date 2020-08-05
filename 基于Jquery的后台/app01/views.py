from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

# from 基于Jquery的后台.utils import encryption_md5
from app01 import models


class LoginViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        msg = ''
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        print(name)
        print(pwd)
        # pwd = encryption_md5(pwd)
        if name == 'he' and pwd == '123456':
            req = redirect('/index')
            req.set_cookie('name', name)
            return req
        else:
            msg = "用户名或密码错误"

        return render(request, 'login.html', {'msg': msg})


class index(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        cxt = {
            'name': name,
        }
        return render(request, 'index.html', cxt)

    def post(self, request, *args, **kwargs):
        pass


class teacher(View):
    def get(self, request, *args, **kwargs):
        cname = request.COOKIES.get('name')
        tea_list = models.Teacher.objects.all()
        for teas in tea_list:
            teas.class_name = ','.join([i.cla_name for i in teas.classes_set.all()])
        cxt = {
            'tea_list': tea_list,
            'name': cname,
        }
        return render(request, 'teacher.html', cxt)

    def post(self, request, *args, **kwargs):
        pass


class student(View):
    def get(self, request, *args, **kwargs):
        cname = request.COOKIES.get('name')
        # c1 =models.Student.objects.create(name='小撒旦',classes_id=2)
        stu_list = models.Student.objects.all()
        for stu_li in stu_list:
            stu_l = stu_li.classes_id
            stu_li.classes_name = models.Classes.objects.get(pk=stu_l).cla_name
            tea_name = models.Classes.objects.get(pk=stu_l)
            stu_li.teacher_name = ','.join([i.name for i in tea_name.teacher.all()])

        cxt = {
            'stu_list': stu_list,
            'name': cname,
        }
        return render(request, 'student.html', cxt)

    def post(self, request, *args, **kwargs):
        pass


class classes(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        # c1 = models.Classes.objects.filter(cla_name='一年级').first()
        # c1.teacher.add(1)
        # c2 = models.Classes.objects.filter(cla_name='二年级').first()
        # c2.teacher.add(3)
        # c3 = models.Classes.objects.filter(cla_name='三年级').first()
        # c3.teacher.add(2)
        cls_list = models.Classes.objects.all()
        for clss in cls_list:
            clss.teacher_name = ','.join([i.name for i in clss.teacher.all()])

        cxt = {
            'cls_list': cls_list,
            'name': name,
        }
        return render(request, 'classes.html', cxt)

    def post(self, request, *args, **kwargs):
        pass


class Update_student(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        stu_id = request.GET.get('update_student_id')
        stu_list = models.Student.objects.get(pk=stu_id)
        cla_list = models.Classes.objects.all()
        for clss in cla_list:
            clss.teacher_name = ','.join([i.name for i in clss.teacher.all()])
        cxt = {
            'stu_list': stu_list,
            'cla_list': cla_list,
            'name': name,
        }
        return render(request, 'update_student.html', cxt)

    def post(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        stu_id = request.POST.get('update_student_id')
        stu = models.Student.objects.get(id=stu_id)
        stu_name = request.POST.get('stu_name')
        cls_id = request.POST.get('cls_id')
        stu.name = stu_name
        stu.classes_id = cls_id
        stu.save()
        cxt = {
            'name': name,
        }
        return render(request, 'index.html', cxt)


class Update_teacher(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        tea_id = request.GET.get('update_teacher_id')
        tea_list = models.Teacher.objects.get(pk=tea_id)
        cla_list = models.Classes.objects.all()
        for clss in cla_list:
            clss.teacher_name = ','.join([i.name for i in clss.teacher.all()])
        cxt = {
            'tea_list': tea_list,
            'cla_list': cla_list,
            'name': name,
        }
        return render(request, 'update_teacher.html', cxt)

    def post(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        stu_id = request.POST.get('update_teacher_id')
        tea = models.Teacher.objects.get(id=stu_id)
        tea_name = request.POST.get('tea_name')
        cls_id = request.POST.get('cls_id')
        Cls_id = models.Classes.objects.filter(pk__in=cls_id)
        tea.name = tea_name
        tea.save()
        for cls in Cls_id:
            tea.classes_set.add(cls)
        tea.save()
        cxt = {
            'name': name,
        }
        return render(request, 'index.html', cxt)


class Update_classes(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        cla_id = request.GET.get('update_classes_id')
        cla_list = models.Classes.objects.get(pk=cla_id)
        tea_list = models.Teacher.objects.all()
        for teas in tea_list:
            teas.teacher_name = ','.join([i.cla_name for i in teas.classes_set.all()])
        cxt = {
            'tea_list': tea_list,
            'cla_list': cla_list,
            'name': name,
        }
        return render(request, 'update_classes.html', cxt)

    def post(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        cla_id = request.POST.get('update_classes_id')
        cla = models.Classes.objects.get(id=cla_id)
        cla_name = request.POST.get('cla_name')
        Tea_id = models.Teacher.objects.all()
        cla.cla_name = cla_name
        cla.save()
        for tea in Tea_id:
            cla.teacher.add(tea)
        cla.save()
        cxt = {
            'name': name,
        }
        return render(request, 'index.html', cxt)


class Delete_student(View):
    def get(self, request, *args, **kwargs):
        delete_id = request.GET.get('delete_student_id')
        stu = models.Student.objects.filter(id=delete_id)
        if stu:
            stu.delete()
            return redirect('/index/')
        return render(request, 'index.html')


class Delete_teacher(View):
    def get(self, request, *args, **kwargs):
        delete_id = request.GET.get('delete_teacher_id')
        tea = models.Teacher.objects.filter(id=delete_id)
        if tea:
            tea.delete()
            return redirect('/index/')
        return render(request, 'index.html')


class Delete_classes(View):
    def get(self, request, *args, **kwargs):
        delete_id = request.GET.get('delete_classes_id')
        cla = models.Classes.objects.filter(id=delete_id)
        if cla:
            cla.delete()
            return redirect('/index/')
        return render(request, 'index.html')


class Add_teacher(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        cla_list = models.Classes.objects.all()
        cxt = {
            'name': name,
            'cla_list': cla_list,
        }

        return render(request, 'add_teacher.html', cxt)

    def post(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        tea_name = request.POST.get('tea_name')
        cls_id = request.POST.getlist('cls_id')
        Cls_id = models.Classes.objects.filter(pk__in=cls_id)

        teacher = models.Teacher()
        teacher.name = tea_name
        teacher.save()
        for cls in Cls_id:
            teacher.classes_set.add(cls)
        teacher.save()
        cxt = {
            'name': name,
        }
        return render(request, 'index.html', cxt)


class Add_classes(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        tea_list = models.Teacher.objects.all()
        cxt = {
            'name': name,
            'tea_list': tea_list,
        }

        return render(request, 'add_classes.html', cxt)

    def post(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        cla_name = request.POST.get('cls_name')
        tea_id = request.POST.getlist('tea_id')
        Tea_id = models.Teacher.objects.filter(pk__in=tea_id)

        Cls = models.Classes()
        Cls.cla_name = cla_name
        Cls.save()
        for cls in Tea_id:
            Cls.teacher.add(cls)
        Cls.save()
        cxt = {
            'name': name,
        }
        return render(request, 'index.html', cxt)


class Add_student(View):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        cla_list = models.Classes.objects.all()
        cxt = {
            'name': name,
            'cla_list': cla_list,
        }

        return render(request, 'add_student.html', cxt)

    def post(self, request, *args, **kwargs):
        name = request.COOKIES.get('name')
        stu_name = request.POST.get('stu_name')
        cls_id = request.POST.get('cls_id')


        stu = models.Student()
        stu.name = stu_name
        stu.classes_id = cls_id
        stu.save()

        cxt = {
            'name': name,
        }
        return render(request, 'index.html', cxt)



class Classes_list(View):
    def get(self, request, *args, **kwargs):
        cname = request.COOKIES.get('name')

        cla_id = request.GET.get('cha_classes_id')
        cla_list = models.Classes.objects.get(pk=cla_id)
        stu_list = cla_list.student_set.all()
        cla_list.teacher_name = ','.join([i.name for i in cla_list.teacher.all()])
        cxt = {
            'stu_list': stu_list,
            'cla_list': cla_list,
            'name': cname,
        }

        return render(request, 'classes_list.html', cxt)

    def post(self, request, *args, **kwargs):
        pass
