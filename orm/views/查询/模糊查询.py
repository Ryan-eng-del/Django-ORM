

from orm.models import Student
from django.shortcuts import HttpResponse
from django.utils import timezone as datetime


def select(request):
    stu = Student.objects.filter(name__contains="彭").values("name", "id")
    stu = Student.objects.filter(name__startswith="彭").values("name", "id")
    stu = Student.objects.filter(name__isnull=True).values("name")
    stu = Student.objects.filter(name__in=["吴彦祖"]).values("name")
    stu = Student.objects.filter(id__gt=1).values("name")
    stu = Student.objects.filter(id__gte=1).values("name")
    stu = Student.objects.filter(id__lt=1).values("name")
    stu = Student.objects.filter(id__lte=1).values("name")
    stu = Student.objects.filter(id__range=[2, 3]).values("name")
    stu = Student.objects.filter(
        created_time__year=2021).values("name")
    stu = Student.objects.filter(created_time__gte=datetime.datetime(
        2016, 6, 20), created_time__lt=datetime.datetime(2016, 6, 21)).all()
    print(stu)
    return HttpResponse("success!")
