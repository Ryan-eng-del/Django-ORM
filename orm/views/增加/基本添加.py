from orm.models import Student
from django.shortcuts import HttpResponse


def add(request):
    print(request, "request", type(request))
    # 方式1
    # stu = Student(name="彭于晏", classmate="计科一班")
    stu = Student(name="彭于晏", classmate="计科一班", sex=0)
    stu.save()

    # 方式2
    # Student.objects.create(name="吴彦祖", classmate="软件一班")

    return HttpResponse("success!")
