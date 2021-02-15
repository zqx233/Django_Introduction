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
    path('filter/', views.handle_filter, name='filter'),
    # 内建标签
    path('tag/', views.handle_tag, name='tag'),
    # include标签
    path('include/', views.include_div, name='include'),
    # 模板中url
    path('url/', views.handle_url, name='url'),
    # 模板继承
    path('extends/', views.handle_extends, name='extends'),
    # 静态资源
    path('wenzhang/', views.handle_static, name='wenzhang')
]
