from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Car(models.Model):
    VIBOR = (('white', 'white'), ('black', 'black'), ('red', 'red'), ('blue', 'blue'), ('violet', 'violet'),
             ('pink', 'pink'), ('yellow', 'yellow'))
    brand = models.CharField(max_length=20, verbose_name='марка', blank=True)
    cost = models.IntegerField(verbose_name='цена', blank=True)
    year = models.IntegerField(verbose_name='год выпуска', blank=True)
    color = models.CharField(max_length=20, choices=VIBOR, verbose_name='цвет', blank=True)


class Company(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    name = models.CharField(max_length=20)
    cost = models.IntegerField()
    firma = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    title = models.CharField(max_length=10)
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.title}'


class Student(models.Model):
    name = models.CharField(max_length=20)
    group = models.CharField(max_length=6)
    courses = models.ManyToManyField(Course)
    receives_scholarship = models.BooleanField(default=False)
    GPA = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=1.0)

    def courses_display(self):
        res = ''
        for one in self.courses.all():
            res += ' ' + one.title
        return res

    def __str__(self):
        return f'{self.name}'
