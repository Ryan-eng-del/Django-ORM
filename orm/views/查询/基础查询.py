from orm.models import Student
from django.shortcuts import HttpResponse


def select(request):
    students = Student.objects.all()
    print(students, "students")

    students = Student.objects.filter(name="彭于晏", sex=1, age=0)
    print(students)

    # 只能返回一个，返回多个会报错
    stu = Student.objects.get(name="吴彦祖")
    print(stu, stu.name, stu.age, type(stu))

    students = Student.objects.filter(name="彭于晏", sex=1, age=0).count()

    students = Student.objects.filter(
        name="彭于晏", sex=1, age=0).order_by("id")
    print(students)

    students = Student.objects.filter(name="cyan", sex=1, age=0).exists()

    students = Student.objects.filter(
        name="彭于晏", sex=1, age=0).values_list("name", "id")

    print(students)
    students = Student.objects.filter(
        name="彭于晏", sex=1, age=0).values("name", "id")

    students = Student.objects.filter(
        name="彭于晏", sex=1, age=0).values("name").distinct()

    print(students)
    return HttpResponse("success!")
