from django.db import models


class Classes(models.Model):
    caption = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32, null=True)
    cls = models.ForeignKey(to=Classes, on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ManyToManyField(to=Classes)


class Administrator(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class Province(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=32)
    pro = models.ForeignKey(to=Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Xian(models.Model):
    name = models.CharField(max_length=32)
    cy = models.ForeignKey(to=City, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    m = models.ManyToManyField(to=Book)

    def __str__(self):
        return self.name

#
# class A_to_B(models.Model):
#     bid = models.ForeignKey(Book)
#     aid = models.ForeignKey(Author)
#
#     class Meta:
#         unique_together = (
#             ('bid','aid'),
#         )
