# Django入门

Django2.2[中文文档](https://docs.djangoproject.com/zh-hans/2.2/)
# Django项目创建
## 创建项目

1. 在PyCharm中新建项目，选择虚拟python环境，然后在PyCharm中安装Django库，可以使用豆瓣等国内镜像快一点。安装好后可以在终端中执行`import django` `django.get_version()`如果没报错即安装成功。
1. 新建好项目之后，在终端中的项目目录下执行`django-admin startproject hello`即可创建django项目，会在目录中生成项目文件。结构如下
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1826767/1610025373054-41979386-7a44-4932-b4a3-e929e8f28842.png#align=left&display=inline&height=104&margin=%5Bobject%20Object%5D&name=image.png&originHeight=104&originWidth=210&size=19723&status=done&style=shadow&width=210)
1. 在终端中的项目目录下运行`python manage.py runserver`即可运行django框架，点击终端显示的链接如果有成功界面即运行成功。
1. 创建好项目后，需要修改项目配置文件setting.py
```
DEBUG = True

# 跟路由
ROOT_URLCONF = 'hello.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # 模板目录，默认在应用下
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 语言和时区，默认英文，可改成中文
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 不使用世界时，改为false，数据库存储的时间和当地时间一致
USE_TZ = False

# 静态资源请求路径
STATIC_URL = '/static/'
```
## 创建应用
一个项目中可以包含多个应用，在项目目录下的命令行中执行`python manage.py startapp 应用名称`，就会创建一个应用。
创建好应用后要在项目配置文件setting.py中修改。
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '应用名称',   #把自己的应用安装，否则不能用
]
```
# 路由url
在Web中发出请求时，Django会获取url中的路径（端口之后的部分），然后通过项目下的urls.py查找与路径匹配的视图，然后返回。在urls.py中，通过urlpatterns列表来定义url和视图之间的映射。如：
```
from django.conf.urls import patterns, include
from app import views

urlpatterns = [
 path('hello/', views.hello, name='hello'),
 path('blog/', include('blog.urls')),
]
```
## path对象
path对象有4个参数

- 模式串：匹配用户请求路径和字符串，模式串最后最好加上/，在url中没有输入最后的/，Django通过重定向也能匹配到。
- 视图函数：匹配到路径后调用的视图函数名
- kwargs：可选参数，需要额外传递的参数，是一个字典
- name：给路由命名，在代码中可以使用name反向解析，和视图函数参数无关

如果path中的模式串不能满足需求，还可以使用re_path，可用正则表达式设定模式串规则
### 模式串
Django检查url模式时会移除模式前的/，所以模式串中可以不写前面的/，但是末尾最好写。模式匹配时，会从urlpatterns列表中从上到下进行匹配，一旦匹配成功则不会继续往下；一个视图函数可以有多个模式匹配；如果匹配失败，则会引起异常。
url不仅是静态的，也可以是动态匹配，向视图传递参数，在path中，有四种类型：

- str：如果没有指定，默认是字符串类型，可以匹配除/和空字符外的其他字符串。
- int：匹配0和正整数，视图函数的参数将得到一个整型值。
- slug：匹配由数字、字母、-和_组成的字符串参数。
- path：匹配任何非空字符串，包括/

因为path类型可以匹配所有字符串 ，所以在设定规则时应该为最后一个类型，因为path会匹配到所有字符串。
# 视图
视图函数的第一个参数就是请求对象，又Django传递
返回给用户的是响应对象
作用，接收并处理请求，调用模型和模板，响应请求
## HttpResquest
是从web服务器传递过来的请求对象，结果Django框架封装产生的，封装了原始的Http请求
