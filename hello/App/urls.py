from django.urls import path, re_path

from . import views
# path第三个参数name是路由的名称，和视图函数参数无关
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^tel/(?P<tel>\d{8})/$', views.get_phone, name='tel'),

    # 响应对象
    path('response/', views.handle_response, name='response'),

    # 重定向
    path('red/', views.handle_redirect, name='red'),
]