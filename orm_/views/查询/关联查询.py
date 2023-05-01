from orm_.models import Student, Course, StudentDetail, Classes
from django.shortcuts import HttpResponse


def select(request):

    # 基于对象查询（子查询）
    # stu = Student.objects.filter(name="彭于晏").get(name="彭于晏")
    # 多对多
    # course = stu.courses.all().values("course_name", "id")
    # 一对多
    # print(stu.stu_class.class_name, course, stu.details.tel, "info")
    # cls = Course.objects.get(course_name="离散数学")
    # print(cls.stu_set, "stu related_name")

    # stu = Student.objects.get(name="彭于晏")
    # cls = Course.objects.get(course_name="高数", id=2)
    # stu.courses.add(cls)

    # stu = Student.objects.get(name="彭于晏")
    # print(stu.courses.all())

    # 多对多 反向查询
    # course = Course.objects.get(course_name="离散数学")
    # print(course, "course")
    # print(course.students.all())

    # 1对1 反向查询
    # detail = StudentDetail.objects.get(id=1)
    # print(detail, "detail")
    # print(detail.students.name)

    # 1对多 反向查询
    # cls = Classes.objects.get(id=1)
    # print(cls.students.all())

    # students = Student.objects.filter(sex=1)
    # arr = []

    # for stu in students:
    #     arr.append(stu.courses.all())

    # print(arr, "courses============")
    return HttpResponse("success!")
