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
是从web服务器传递过来的请求对象，结果Django框架封装产生的，封装了原始的Http请求。

常见用法如下

```python
# request常用属性
# get传参的获取
print(request.GET)  # GET quersetDict，不能修改
# 获取单一值
print(request.GET.get('username'))  # 如果username不存在，会返回None
print(request.GET['username'])  # 如果username不存在，会报错
# 获取多值
print(request.GET.getlist('age'))  # 返回值是一个列表

# POST传参
print(request.POST.get('username'))
print(request.POST.getlist('hobby'))

# 获取请求方法
print(request.method)  # 返回方法是GET或POST　

# 获取请求路径
print(request.path)

# 其他请求属性
print(request.META)

# 客户端地址
print(request.META.get('REMOTE_ADDR'))
# 来源页面
print(request.META.get('HTTP_REFERER'))

# 常用方法
print(request.get_full_path())  # 请求路径＋查询字符串
print(request.get_host())  # 主机名和端口
print(request.build_absolute_uri())  # 完整的url

# 获取请求参数的字典 由queryDict转dict
print(request.GET.dict())
```

其中，QueryDict是Dict的子类，所有的值都是列表，用于存储从请求中传递来的参数。

* HttpRequest中的QueryDict是不可变的，只能获取值，不能修改。
* QueryDict键值对都是字符串
* QueryDict中一个键可以对应多个值

## HttpResponse

每一个视图必须返回一个响应对象，HttpResponse对象由程序员创建并返回。

常用方法如下：

```python
def handle_response(request):
    res = HttpResponse("响应对象")
    res.content_type = "text/html"
    res.status_code = 400 # 人为设置状态码
    return res

    # render返回响应对象，render只是HttpResponse的包装，还是会返回一个HttpResponse对象，第二个参数为模板，context参数为向模板传递的变量
    res = render(request, 'Appindex.html', context = '变量名': '值')
    return res

    # jsonresponse 可以返回json字符串，一般时候可以把字典，列表转换为json返回给前端，字典，列表只能包含内置类型
    return JsonResponse({'name': 'tom'})
    # 如果参数不是字典，必须把safe设置为false
    return JsonResponse([1, 2, 3, 4, 5], safe=False)
```

## 重定向

服务端发现收到的请求要求获取的资源在另一个位置时，可以使用重定向发起新的请求访问正确的资源位置。

```python
def handle_redirect(request):
    # 重定向到指定路由地址，参数就是路由
    return HttpResponseRedirect('/app/')
    # 可用缩写
    return redirect('/app/')
	# 应用外跳转，参数为绝对地址
    return redirect('https://www.baidu.com')
    # 带参数重定向
    return redirect('/app/tel/{}/'.format('12345678'))
    return redirect('/app/tel/12345678')

    # 反向定位：由应用的命名空间：name来确定路由，应用命空间见url.py
    return redirect(reverse('App:index'))  # 不带参数
    # 带参数，如果参数有名字，必须使用关键字传参的方式
    return redirect(reverse('App:tel', kwargs={'tel': '12345678'}))
    # 没名字，用args传参，可以时列表或元组
    return redirect(reverse('App:tel', args=('12345678',)))  # 元组只有一个元素的话后面要加，
```

## 错误视图

### 404错误及视图

url匹配失败后，Django会调用内置的404模板显示，在开发阶段开启调试模式时，会显示详细信息，在产品上线时应关闭，关闭后会显示一个标准的错误页面。

```
# setting.py
DEBUG = False
```

404页面可以自定义，在项目templates目录中添加404.html，在setting.py中设置好模板路径，Django需要显示404页面时就会调用该界面。

```
# 模板配置
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        ...
    },
]
```

其他错误视图方法一致。

# 模板

模板⽤于快速⽣成动态⻚⾯返回给客户端，模板是⼀个⽂本，⽤于分离⽂档的表现 形式和内容。 模板定义了占位符以及各种⽤于规范⽂档该如何显示的模板标签。 模板通常⽤于产⽣HTML，但是Django的模板也能产⽣任何基于⽂本格式的⽂档。 模板包含两部分：

- html代码
- 模板标签

## 模板位置

1. 模板可以放在应用中的`templates`目录，不需要注册，但有多个应用的时候不能复用页面

2. 模板也可以放在工程局目录下的`templates`目录下，如果有多个应用，可以调用相同的页面，需要注册，修改项目配置文件`setings.py`

   ```
   TEMPLATES = [
       {
           ......
           'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 模板目录，默认在应用下
           'APP_DIRS': True,  # 是否在应用目录下查找模板文件
           ......
               ],
           },
       },
   ]
   ```

Django在查找模板时，不是只在当前app的模板文件中查找，而是在所有app的模板目录中查找，一旦找到就停止，所以如果模板名字相同时可能会找错，可以在应用模板目录下再建立一个app同名模板文件夹解决，建议都放在工程模板目录下方便管理。

## 模板渲染

就是将html中的标签替换掉

### loader加载

可以加载一次模板，然后进行多次渲染

```
def load_template(request):
    # 加载模板文件，生成模板对象
    obj = loader.get_template('example.html')
    res = obj.render({'name': 'admin'})
    # 渲染的结果生成html源文件（字符串）
    return HttpResponse(res)
```

### render

```
def load_template(request):
	# render加载和渲染一起进行，是一种快捷方式
    return render(request, 'example.html', context={'name':'admin'})
```

## 模板语法

### 变量

在html中，使用变量格式为`{{ 变量名 }}`，变量名就是render中context的键

- 列表、元组时，可以使用索引，但不能使用负索引，格式：变量.索引

- 字典时，格式：变量.key

- 对象时，格式：对象.属性   对象.方法名（方法不能有参数）

当模板系统遇到.时，按照以下顺序查找

- 字典
- 属性
- 方法
- 列表索引

如果模板中引用的变量未传值，则会被置为空，不会报错，除非对其进行了操作

### 过滤器

过滤器是在变量显示之前修改值的一个方法，格式为`{{ 变量名|方法:参数 }}`，过滤器可以串联调用，具体内置过滤器方法见[官方文档](https://docs.djangoproject.com/zh-hans/2.2/ref/templates/builtins/#filters)。

#### 自定义过滤器

- 在app目录下新建一个包：templatetags
- 在包中创建一个py文件

```
from django import template

# 建立模板对象
register = template.Library()

# name表示在模板中使用的过滤器名称
@register.filter(name='sub1')
def sub(value):  # 参数必须是1~2个
    return value - 1
```

- 在模板中引用

```
{% load mytag %} # 加载⾃定义过滤器的模块
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <title>Title</title>
</head>
<body>
{{ 5|sub1 }} # 使⽤⾃定义过滤器
</body>
</html>
```

### 内建标签

格式：`{% tag %}`

1. if标签

   ```html
   <body>
   {# 不可以使用小括号，可以嵌套 #}
   {% if num < 10 %}
   <p>
       小于10
   </p>
   {% elif num < 20 %}
   <p>
       小于20
   </p>
   {% else %}
   <p>
       其他
   </p>
   {% endif %}
   </body>
   ```

2. for标签

   ```
   <p>
       {% for value in l1 reversed %}  加reversed可以实现反向遍历
   <li>{{ value }}</li>
       {% empty %}
   数据不存在
   {% endfor %}
   </p>
   ```

   

# 一些遇到的问题

## 解决Debug页面有时无法显示正常错误信息

使用runserver运行后，出错信息无法正常显示在控制台和前端，控制台显示`UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 9737: illegal multibyte sequence`，前端页面显示`A server error occurred. Please contact the administrator.`

解决方法：打开`python安装路径\Lib\site-packages\django\views\debug.py`修改约为331行处的代码：

```
with Path(CURRENT_DIR, 'templates', 'technical_500.html').open() as fh:
```

修改为：

```
with Path(CURRENT_DIR, 'templates', 'technical_500.html').open(encoding='utf-8') as fh:
```

可能是因为文件中有中文导致无法正常显示。

> 参考链接：https://blog.csdn.net/qq_37232731/article/details/89684409

