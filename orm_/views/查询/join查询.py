from orm_.models import Student, Classes
from django.shortcuts import HttpResponse
from django.utils import timezone as datetime
from django.db.models import F, Q, Sum, Avg, Max, Min, Count


def select(request):
    stu = Student.objects.filter(name="彭于晏").values(
        "name", "stu_class__class_name", "sex")

    stu = Classes.objects.filter(students__name="彭于晏").values(
        "class_name", "students__name", "students__sex")

    print(stu)

    return HttpResponse("success!")
