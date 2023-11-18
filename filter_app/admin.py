from django.contrib import admin
from filter_app.models import *


# Register your models here.
# admin.site.register(Car)


# class CarAdmin(admin.ModelAdmin):
#     list_display = ('brand', 'cost', 'year', 'color')
#
#
# admin.site.register(Car, CarAdmin)
@admin.register(Car)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('brand', 'cost', 'year', 'color')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'firma')
    fields = ('name', 'cost', 'firma')
    list_display_links = ('name', 'firma')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'courses_display')
