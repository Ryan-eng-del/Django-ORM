from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        abstract = True


class Cls(BaseModel):
    class_name = models.CharField(max_length=32, db_index=True)

    class Meta:
        db_table = "class"

    def __str__(self):
        return "<Class %s>" % self.class_name


class Course(BaseModel):
    course_name = models.CharField(max_length=32, db_index=True)

    class Meta:
        db_table = "course"

    def __str__(self):
        return "<Course %s>" % self.course_name


class StudentDetail(models.Model):
    tel = models.CharField(max_length=32)
    email = models.EmailField()

    class Meta:
        db_table = "student_detail"


class Student(BaseModel):
    SEX_CHOICES = ((0, "男生"), (1, "女生"), (2, "保密"))
    name = models.CharField(max_length=32, verbose_name="学生姓名", db_index=True)
    age = models.SmallIntegerField(verbose_name="年龄", default=0)
    sex = models.SmallIntegerField(
        choices=SEX_CHOICES, default=1, verbose_name="性别")
    # 不能用 class 因为是 python 的保留字， 也可以通过 db_column 来自定义列名
    # classmate = models.CharField(
    #     db_column="class", max_length=5, db_index=True, verbose_name="班级")

    description = models.TextField(default="", verbose_name="个性签名")
    stu_class = models.ForeignKey(
        to="Cls", on_delete=models.CASCADE, related_name="stu_class", db_column='class')
    courses = models.ManyToManyField(
        "Course", db_table="student_course", related_name="stu_course")
    details = models.OneToOneField(
        "StudentDetail", on_delete=models.CASCADE, related_name="stu_details")

    class Meta:
        db_table = "student"
        verbose_name = "学生信息表"

    def __str__(self):
        return "<Student %s>" % self.course_name
