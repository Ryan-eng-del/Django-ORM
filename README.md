## 介绍

针对于 Django ORM 进行训练的仓库

## 模型层（ORM）

Django 中内嵌了 ORM 框架，不需要直接编写 SQL 语句进行数据库操作，而是通过定义模型类，操作模型类来完成对数据库中表的增删改查和创建等操作。

![image-20211008150813304](assets/image-20211008150813304.png)

> O 是 object，也就**类对象**的意思。
>
> R 是 relation，翻译成中文是关系，也就是关系数据库中**数据表**的意思。
>
> M 是 mapping，是**映射**的意思。

映射：

> 类：sql 语句 table 表
>
> 类成员变量：table 表中的字段、类型和约束
>
> 类对象：sql 表的表记录

ORM 的优点

> - 数据模型类都在一个地方定义，更容易更新和维护，也利于重用代码。
>
> - ORM 有现成的工具，很多功能都可以自动完成，比如数据消除、预处理、事务等等。
>
> - 它迫使你使用 MVC 架构，ORM 就是天然的 Model，最终使代码更清晰。
>
> - 基于 ORM 的业务代码比较简单，代码量少，语义性好，容易理解。
>
> - 新手对于复杂业务容易写出性能不佳的 SQL,有了 ORM 不必编写复杂的 SQL 语句, 只需要通过操作模型对象即可同步修改数据表中的数据.
>
> - 开发中应用 ORM 将来如果要切换数据库.只需要切换 ORM 底层对接数据库的驱动【修改配置文件的连接地址即可】

ORM 也有缺点

> - ORM 库不是轻量级工具，需要花很多精力学习和设置，甚至不同的框架，会存在不同操作的 ORM。
> - 对于复杂的业务查询，ORM 表达起来比原生的 SQL 要更加困难和复杂。
> - ORM 操作数据库的性能要比使用原生的 SQL 差。
> - ORM 抽象掉了数据库层，开发者无法了解底层的数据库操作，也无法定制一些特殊的 SQL。【自己使用 pymysql 另外操作即可，用了 ORM 并不表示当前项目不能使用别的数据库操作工具了。】

我们可以通过以下步骤来使用 django 的数据库操作

```text
1. 配置数据库连接信息
2. 在models.py中定义模型类
3. 生成数据库迁移文件并执行迁文件[注意：数据迁移是一个独立的功能，这个功能在其他web框架未必和ORM一块的]
4. 通过模型类对象提供的方法或属性完成数据表的增删改查操作
```

## 6.1、配置数据库连接

在 settings.py 中保存了数据库的连接配置信息，Django 默认初始配置使用**sqlite**数据库。

1. 使用**MySQL**数据库首先需要安装驱动程序

   ```shell
   pip install PyMySQL
   ```

2. 在 Django 的工程同名子目录的`__init__`.py 文件中添加如下语句

   ```python
   from pymysql import install_as_MySQLdb
   install_as_MySQLdb() # 让pymysql以MySQLDB的运行模式和Django的ORM对接运行
   ```

   作用是让 Django 的 ORM 能以 mysqldb 的方式来调用 PyMySQL。

3. 修改**DATABASES**配置信息

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'HOST': '127.0.0.1',  # 数据库主机
           'PORT': 3306,  # 数据库端口
           'USER': 'root',  # 数据库用户名
           'PASSWORD': '123',  # 数据库用户密码
           'NAME': 'student'  # 数据库名字
       }
   }
   ```

4. 在 MySQL 中创建数据库

   ```mysql
   create database student; # mysql8.0默认就是utf8mb4;
   create database student default charset=utf8mb4; # mysql8.0之前的版本
   ```

5. 注意 3: 如果想打印 orm 转换过程中的 sql，需要在 settings 中进行如下配置：

   ```python
   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'console':{
               'level':'DEBUG',
               'class':'logging.StreamHandler',
           },
       },
       'loggers': {
           'django.db.backends': {
               'handlers': ['console'],
               'propagate': True,
               'level':'DEBUG',
           },
       }
   }　　
   ```

## 6.2、定义模型类

定义模型类

> - 模型类被定义在"子应用/models.py"文件中。
> - 模型类必须直接或者间接继承自 django.db.models.Model 类。

接下来以学生管理为例进行演示。[系统大概 3-4 表，学生信息，课程信息，老师信息]，创建子应用 student，注册子应用并引入子应用路由.

settings.py，代码：

```python
INSTALLED_APPS = [
	# ...
    'student',
]
```

urls.py，总路由代码：

```python
urlpatterns = [
    # 省略，如果前面有重复的路由，改动以下。
    path("student/", include("student.urls")),
]
```

在 models.py 文件中定义模型类。

```python
from django.db import models
from datetime import datetime

# 模型类必须要直接或者间接继承于 models.Model
class BaseModel(models.Model):
	"""公共模型[公共方法和公共字段]"""
	# created_time = models.IntegerField(default=0, verbose_name="创建时间")
	created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	# auto_now_add 当数据添加时设置当前时间为默认值
	# auto_now= 当数据添加	/更新时, 设置当前时间为默认值
	updated_time = models.DateTimeField(auto_now=True)
	class Meta(object):
		abstract = True # 设置当前模型为抽象模型, 当系统运行时, 不会认为这是一个数据表对应的模型.

class Student(BaseModel):
	"""Student模型类"""
	#1. 字段[数据库表字段对应]
	SEX_CHOICES = (
		(0,"女"),
		(1,"男"),
		(2,"保密"),
	)

	# 字段名 = models.数据类型(约束选项1,约束选项2, verbose_name="注释")
	# SQL: id bigint primary_key auto_increment not null comment="主键",
    # id = models.AutoField(primary_key=True, null=False, verbose_name="主键") # django会自动在创建数据表的时候生成id主键/还设置了一个调用别名 pk

    # SQL: name varchar(20) not null comment="姓名"
    # SQL: key(name),
    name = models.CharField(max_length=20, db_index=True, verbose_name="姓名" )

    # SQL: age smallint not null comment="年龄"
    age = models.SmallIntegerField(verbose_name="年龄")

    # SQL: sex tinyint not null comment="性别"
    # sex = models.BooleanField(verbose_name="性别")
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=2)

    # SQL: class varchar(5) not null comment="班级"
    # SQL: key(class)
    classmate = models.CharField(db_column="class", max_length=5, db_index=True, verbose_name="班级")
    # SQL: description longtext default "" not null comment="个性签名"
    description = models.TextField(default="", verbose_name="个性签名")

	#2. 数据表结构信息
	class Meta:
		db_table = 'tb_student'  # 指明数据库表名,如果没有指定表明,则默认为子应用目录名_模型名称,例如: users_student
		verbose_name = '学生信息表'  # 在admin站点中显示的名称
		verbose_name_plural = verbose_name  # 显示的复数名称

	#3. 自定义数据库操作方法
	def __str__(self):
		"""定义每个数据对象的显示信息"""
		return "<User %s>" % self.name
```

#### （1） 数据库表名

模型类如果未指明表名 db*table，Django 默认以 \*\*小写 app 应用名*小写模型类名\*\* 为数据库表名。

可通过**db_table** 指明数据库表名。

#### （2） 关于主键

django 会为表创建自动增长的主键列，每个模型只能有一个主键列。

如果使用选项设置某个字段的约束属性为主键列(primary_key)后，django 不会再创建自动增长的主键列。

```python
class Student(models.Model):
    # django会自动在创建数据表的时候生成id主键/还设置了一个调用别名 pk
    id = models.AutoField(primary_key=True, null=False, verbose_name="主键") # 设置主键
```

默认创建的主键列属性为 id，可以使用<mark>pk</mark>代替，pk 全拼为<mark>primary key</mark>。

#### （3） 属性命名限制

- 不能是 python 的保留关键字。

- 不允许使用连续的 2 个下划线，这是由 django 的查询方式决定的。\_\_ 是关键字来的，不能使用！！！

- 定义属性时需要指定字段类型，通过字段类型的参数指定选项，语法如下：

  ```python
  属性名 = models.字段类型(约束选项, verbose_name="注释")
  ```

#### （4）字段类型

| 类型             | 说明                                                                                                                                                                                                 |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AutoField        | 自动增长的 IntegerField，通常不用指定，不指定时 Django 会自动创建属性名为 id 的自动增长属性                                                                                                          |
| BooleanField     | 布尔字段，值为 True 或 False                                                                                                                                                                         |
| NullBooleanField | 支持 Null、True、False 三种值                                                                                                                                                                        |
| CharField        | 字符串，参数 max_length 表示最大字符个数，对应 mysql 中的 varchar                                                                                                                                    |
| TextField        | 大文本字段，一般大段文本（超过 4000 个字符）才使用。                                                                                                                                                 |
| IntegerField     | 整数                                                                                                                                                                                                 |
| DecimalField     | 十进制浮点数， 参数 max_digits 表示总位数， 参数 decimal_places 表示小数位数,常用于表示分数和价格 Decimal(max_digits=7, decimal_places=2) ==> 99999.99~ 0.00                                         |
| FloatField       | 浮点数                                                                                                                                                                                               |
| DateField        | 日期<br>参数 auto_now 表示每次保存对象时，自动设置该字段为当前时间。<br>参数 auto_now_add 表示当对象第一次被创建时自动设置当前。<br>参数 auto_now_add 和 auto_now 是相互排斥的，一起使用会发生错误。 |
| TimeField        | 时间，参数同 DateField                                                                                                                                                                               |
| DateTimeField    | 日期时间，参数同 DateField                                                                                                                                                                           |
| FileField        | 上传文件字段,django 在文件字段中内置了文件上传保存类, django 可以通过模型的字段存储自动保存上传文件, 但是, 在数据库中本质上保存的仅仅是文件在项目中的存储路径!!                                      |
| ImageField       | 继承于 FileField，对上传的内容进行校验，确保是有效的图片                                                                                                                                             |

#### （5）约束选项

| 选项        | 说明                                                                                |
| :---------- | ----------------------------------------------------------------------------------- |
| null        | 如果为 True，表示允许为空，默认值是 False。相当于 python 的 None                    |
| blank       | 如果为 True，则该字段允许为空白，默认值是 False。 相当于 python 的空字符串，“”      |
| db_column   | 字段的名称，如果未指定，则使用属性的名称。                                          |
| db_index    | 若值为 True, 则在表中会为此字段创建索引，默认值是 False。 相当于 SQL 语句中的 key   |
| default     | 默认值，当不填写数据时，使用该选项的值作为数据的默认值。                            |
| primary_key | 如果为 True，则该字段会成为模型的主键，默认值是 False，一般不用设置，系统默认设置。 |
| unique      | 如果为 True，则该字段在表中必须有唯一值，默认值是 False。相当于 SQL 语句中的 unique |

**注意：null 是数据库范畴的概念，blank 是表单验证范畴的**

#### （6） 外键

在设置外键时，需要通过**on_delete**选项指明主表删除数据时，对于外键引用表数据如何处理，在 django.db.models 中包含了可选常量：

- **CASCADE** 级联，删除主表数据时连通一起删除外键表中数据

- **PROTECT** 保护，通过抛出**ProtectedError**异常，来阻止删除主表中被外键应用的数据

- **SET_NULL** 设置为 NULL，仅在该字段 null=True 允许为 null 时可用

- **SET_DEFAULT** 设置为默认值，仅在该字段设置了默认值时可用

- **SET()** 设置为特定值或者调用特定方法，例如：

  ```python
  from django.conf import settings
  from django.contrib.auth import get_user_model
  from django.db import models

  def get_sentinel_user():
      return get_user_model().objects.get_or_create(username='deleted')[0]

  class UserModel(models.Model):
      user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.SET(get_sentinel_user),
      )
  ```

- **DO_NOTHING** 不做任何操作，如果数据库前置指明级联性，此选项会抛出**IntegrityError**异常

商品分类表

| id  | category |     |
| --- | -------- | --- |
| 1   | 蔬菜     |     |
| 2   | 电脑     |     |

商品信息表

| id  | goods_name    | cid |
| --- | ------------- | --- |
| 1   | 冬瓜          | 1   |
| 2   | 华为笔记本 A1 | 2   |
| 3   | 茄子          | 1   |

> 1. 当模型字段的 on_delete=CASCADE, 删除蔬菜（id=1），则在外键 cid=1 的商品 id1 和 3 就被删除。
>
> 2. 当模型字段的 on_delete=PROTECT，删除蔬菜，mysql 自动检查商品信息表，有没有 cid=1 的记录，有则提示必须先移除掉商品信息表中，id=1 的所有记录以后才能删除蔬菜。
>
> 3. 当模型字段的 on_delete=SET_NULL，删除蔬菜以后，对应商品信息表，cid=1 的数据的 cid 全部被改成 cid=null
>
> 4. 当模型字段的 on_delete=SET_DEFAULT，删除蔬菜以后，对应商品信息表，cid=1 的数据记录的 cid 被被设置默认值。

## 6.3、数据迁移

将模型类定义表架构的代码转换成 SQL 同步到数据库中，这个过程就是数据迁移。django 中的数据迁移，就是一个类，这个类提供了一系列的终端命令，帮我们完成数据迁移的工作。

#### （1）生成迁移文件

所谓的迁移文件, 是类似模型类的迁移类,主要是描述了数据表结构的类文件.

```python
python manage.py makemigrations
```

#### （2）同步到数据库中

```python
python manage.py migrate
```

补充：在 django 内部提供了一系列的功能，这些功能也会使用到数据库，所以在项目搭建以后第一次数据迁移的时候，会看到 django 项目中其他的数据表被创建了。其中就有一个 django 内置的 admin 站点管理。

```
# admin站点默认是开启状态的，我们可以通过http://127.0.0.1:8000/admin
# 这个站点必须有个管理员账号登录，所以我们可以在第一次数据迁移，有了数据表以后，就可以通过以下终端命令来创建一个超级管理员账号。
python manage.py createsuperuser
```

# from django.db.models import Avg, Count, Max, Min

ret = Student.objects.values("sex").annotate(c = Count("name"))
print(ret) # <QuerySet [{'sex': 0, 'c': 1}, {'sex': 1, 'c': 3}]>

# （1）查询每一个班级的名称以及学生个数

ret = Clas.objects.values("name").annotate(c = Count("student_list\_\_name"))
print(ret) # <QuerySet [{'name': '网络工程 1 班', 'c': 0}, {'name': '网络工程 2 班', 'c': 0}, {'name': '计算机科学与技术 1 班', 'c': 0}, {'name': '计算机科学与技术 2 班', 'c': 1}, {'name': '软件 1 班', 'c': 3}]>

# （2）查询每一个学生的姓名,年龄以及选修课程的个数

ret = Student.objects.values("name","age").annotate(c=Count("courses\_\_title"))
print(ret) # <QuerySet [{'name': 'rain', 'c': 0}, {'name': '张三', 'c': 2}, {'name': '李四', 'c': 2}, {'name': '王五', 'c': 0}]>

ret = Student.objects.all().annotate(c=Count("courses\_\_title")).values("name","age","sex","c")

# print(ret)

# (3) 每一个课程名称以及选修学生的个数

ret = Course.objects.all().annotate(c = Count("students\_\_name")).values("title","c")
print(ret) # <QuerySet [{'title': '近代史', 'c': 2}, {'title': '思修', 'c': 0}, {'title': '篮球', 'c': 1}, {'title': '逻辑学', 'c': 1}, {'title': '轮滑', 'c': 0}]>

# (4) 查询选修课程个数大于 1 的学生姓名以及选修课程个数

ret = Student.objects.all().annotate(c=Count("courses**title")).filter(c**gt=1).values("name","c")
print(ret) # <QuerySet [{'name': '张三', 'c': 2}, {'name': '李四', 'c': 2}]>

# (5) 查询每一个学生的姓名以及选修课程个数并按着选修的课程个数进行从低到高排序

ret = Student.objects.all().annotate(c=Count("courses\_\_title")).order_by("c").values("name","c")
print(ret)
