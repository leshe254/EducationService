from django.contrib import admin

# Register your models here.
from .models import Author, Product, Lession, Group, Student

admin.site.register(Author)
admin.site.register(Product)
admin.site.register(Lession)
admin.site.register(Group)
admin.site.register(Student)
