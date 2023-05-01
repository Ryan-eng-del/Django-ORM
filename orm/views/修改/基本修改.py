from orm.models import Student
from django.shortcuts import HttpResponse


def update(request):
    stu = Student.objects.filter(name="彭于晏", id__lte=3).first()
    print(stu)
    stu.name = "王一博"
    stu.save()
    print(stu)

    stu = Student.objects.filter(
        name="王一博", id__lte=3).update(name="彭于晏", sex=0)
    print(stu)

    stu = Student.objects.filter(
        name="彭于晏").update(name="王一博", sex=0)
    print(stu)

    stu = Student.objects.filter(
        name="王一博").update(name="彭于晏", sex=0)
    print(stu)

    return HttpResponse("success!")
