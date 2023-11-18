from django.shortcuts import render
from filter_app.forms import *
from filter_app.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def car(request):
    # a = Car.objects.get(id=1)
    # print(a, a.brand)
    # b = Car.objects.filter(color='white')
    # print(b.count())
    # for one in b:
    #     print(one.brand)
    # c = Car.objects.filter(cost__lte=100)
    # print(c.count())
    # for one in c:
    #     print(one.brand)
    # d = Car.objects.exclude(cost__lte=100)
    # print(d.count())
    # for one in d:
    #     print(one.brand)
    db = {}
    forma = CarForm()
    if request.POST:
        K1 = request.POST.get('brand')
        K2 = request.POST.get('cost')
        K3 = request.POST.get('year')
        K4 = request.POST.get('color')
        print(K1, K2, K3, K4)
        if K1:
            db = Car.objects.filter(brand=K1)
        elif K2:
            db = Car.objects.filter(cost__lte=K2)
        elif K3:
            db = Car.objects.filter(year=K3)
        elif K4:
            db = Car.objects.filter(color=K4)
    data = {'forma': forma, 'database': db}
    return render(request, 'car.html', data)


def comp(request):
    db = Product.objects.all()
    forma = CompanyForm()
    if request.POST:
        K1 = request.POST.get('pole')
        print(K1)
        db = Company.objects.get(id=K1).product_set.all()
    data = {'database': db, 'forma': forma}
    return render(request, 'comp.html', data)


def stud(request):
    db = Course.objects.all()
    forma = StudentForm()
    param = ' '
    if request.POST:
        a = request.POST.get('poleCourse')
        b = request.POST.get('poleStud')
        c = request.POST.get('poleGPA')
        d = request.POST.get('poleStudHaveScholarship')

        if b and not a and not c and not d:
            db = Student.objects.get(id=b).courses.all()
            param = 'C'
        elif a and not b and not c and not d:
            db = Course.objects.get(id=a).student_set.all()
            param = 'S'
        elif c and not b and not a and not d:
            db = Student.objects.filter(GPA__gte=c)
            param = 'S'
        elif d and not b and not a and not c:
            db = Student.objects.filter(receives_scholarship=1)
            param = 'S'

    data = {'database': db, 'forma': forma, 'key': param}
    return render(request, 'stud.html', data)
