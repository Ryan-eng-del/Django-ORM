from orm.models import Student
from django.shortcuts import HttpResponse
from django.utils import timezone as datetime
from django.db.models import F, Q, Sum, Avg, Max, Min, Count


def select(request):
    stu = Student.objects.exclude(created_time=F("updated_time"))
    stu = Student.objects.filter(Q(name="吴彦祖") | Q(name="彭于晏"))
    stu = Student.objects.filter(
        Q(name="吴彦祖") | Q(name="彭于晏")).aggregate(Avg("age"))
    stu = Student.objects.filter(
        Q(name="吴彦祖") | Q(name="彭于晏")).aggregate(Max("id"))

    # TODO 这里记得回来补全，分组查询
    stu = Student.objects.values("sex").annotate().values(
        "id", "sex", "name")

    ret = Student.objects.raw("SELECT name, id, class FROM student")
    print(ret, type(ret))

    for item in ret:
        print(item, type(item))

    return HttpResponse("success!")
