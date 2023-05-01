from orm_.models import Student, StudentDetail, Classes, Course
from django.shortcuts import HttpResponse


def add(request):
    # 创建用户
    # StudentDetail.objects.create(tel="18835229632", email="cyan0909@163.com")
    # Classes.objects.create(class_name="软件一班")
    # Student.objects.create(name="吴彦祖", details_id=2, stu_class_id=2)\
    # 老师创建班级
    # Classes.objects.create(class_name="离散数学")
    # 用户选课
    # Student.objects.filter(name="彭于晏").update(stu_class_id=1)
    # 老师创建班级
    # cls = Course.objects.create(course_name="离散数学")
    # 获取用户
    # stu = Student.objects.get(name="彭于晏")
    # cls = Course.objects.get(course_name="离散数学")
    # stu.courses.set([cls])
    return HttpResponse("success!")
