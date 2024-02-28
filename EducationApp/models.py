from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    # Продукт может принадлежать только одному автору
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_and_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Lession(models.Model):
    # Урок может принадлежать только одному продукту
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    video_link = models.URLField()

    def __str__(self):
        return self.name


class Group(models.Model):
    # Группа может принадлежать только к одному продукту
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    # В группе может быть много студентов, а так же может быть открыт набор в группы
    students = models.ManyToManyField('Student', blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    # Студент может быть во множестве групп, а так же может и не состоять в группе
    groups = models.ManyToManyField('Group', blank=True, null=True)

    def __str__(self):
        return self.username
