from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    datetime = models.TimeField()
    price = models.IntegerField()


class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    # У одного продукта может быть много уроков
    product_key = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    videolink = models.URLField()


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    # Один продукт может включать в себя много групп
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    name = models.CharField(max_length=100)
    # Одна группа может включать в себя много студентов
    students = models.ForeignKey('Students', on_delete=models.CASCADE)


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    # Студент может быть только в одной группе
    group_id = models.OneToOneField('Group', on_delete=models.CASCADE)
