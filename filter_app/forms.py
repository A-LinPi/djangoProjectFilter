from django import forms
from filter_app.models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'cost', 'year', 'color')


class CompanyForm(forms.Form):
    pole = forms.ModelChoiceField(Company.objects.all())


class StudentForm(forms.Form):
    poleCourse = forms.ModelChoiceField(Course.objects.all(), required=False)
    poleStud = forms.ModelChoiceField(Student.objects.all(), required=False)
