
from django.urls import path
from orm.views.增加 import 基本添加
from orm.views.查询 import 进阶查询, 模糊查询, 基础查询
from orm.views.修改 import 基本修改
from orm.views.删除 import 基本删除


urlpatterns = [
    path('add', 基本添加.add),
    path('select', 基础查询.select),
    # path('select', 模糊查询.select),
    # path('select', 进阶查询.select),
    # path('update', 基本修改.update),
    # path('delete', 基本删除.delete)
]
