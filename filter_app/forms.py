from django import forms
from filter_app.models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'cost', 'year', 'color')


class CompanyForm(forms.Form):
    pole = forms.ModelChoiceField(Company.objects.all())


class StudentForm(forms.Form):
    poleCourse = forms.ModelChoiceField(Course.objects.all(), required=False, label='Поиск студентов по курсам')
    poleStud = forms.ModelChoiceField(Student.objects.all(), required=False, label='Поиск курсов по студентам')
    poleGPA = forms.FloatField(required=False, label='Средний бал (больше)')
    poleStudHaveScholarship = forms.BooleanField(required=False, label='Получает стипендию')
