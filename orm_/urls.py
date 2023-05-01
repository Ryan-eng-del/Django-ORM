

from django.urls import path
from orm_.views.增加 import 基本添加
from orm_.views.查询 import join查询, 关联查询, 分组查询
# from orm_high.views.修改 import 基本修改
# from orm_high.views.删除 import 基本删除


urlpatterns = [
    path('add', 基本添加.add),
    # path('select', 关联查询.select),
    # path('select', join查询.select),
    path('select', 分组查询.select),

    # path('select', 模糊查询.select),
    # path('select', 进阶查询.select),
    # path('update', 基本修改.update),
    # path('delete', 基本删除.delete)
]
