from orm.models import Student
from django.shortcuts import HttpResponse


def delete(request):
    stu = Student.objects.filter(name="彭于晏", id__gt=2).delete()
    print(stu)

    return HttpResponse("success!")
