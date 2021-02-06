from django.urls import path, re_path

from . import views

app_name = 'App02'  # 应用的名空间
# path第三个参数name是路由的名称，和视图函数参数无关
urlpatterns = [
    path('', views.index, name='index'),
    path('render/', views.load_template, name='render'),
    # 变量
    path('var/', views.handle_var, name='var'),
    # 过滤器
    path('filter/', views.handle_filter, name='filter')
]
