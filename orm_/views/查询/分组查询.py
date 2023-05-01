from orm_.models import Student, Classes
from django.shortcuts import HttpResponse
from django.utils import timezone as datetime
from django.db.models import F, Q, Sum, Avg, Max, Min, Count

# SELECT class_name, COUNT(class_name) as student_number FROM class GROUP BY class_name

# SELECT job, MAX(sal) as max_sale, Min(sal) as min_sale FROM class GROUP BY job

# SELECT job, COUNT(job) FROM class WHERE sal < 1500 GROUP BY job

# SELECT job, SUM(sale) as sum  FROM class GROUP BY job HAVING job != "salesmen" AND  sum >= 5000


def select(request):
    cls = Classes.objects.values("class_name").annotate(class_count=Count(
        "class_name")).values("class_name", "class_count").filter(class_count__gt=2)
    cls = Classes.objects.values("class_name").annotate(
        stu_count=Count("students__name")).values("class_name", "stu_count")
    print(cls, "cls")
    return HttpResponse("success!")
