from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    # return HttpResponse()
    # 使用模板引擎开发
    return render(request, 'App02/index.html')


def load_template(request):
    # 加载模板文件，生成模板对象
    # obj = loader.get_template('example.html')
    # print(obj, type(obj))
    # res = obj.render({'name': 'admin'})
    # print(res)
    # # 渲染的结果生成html源文件（字符串）
    # return HttpResponse(res)

    # render加载和渲染一起进行，是一种快捷方式
    return render(request, 'example.html', context={'name': 'admin'})


def handle_var(request):
    num = 10
    name = '一个字符串'
    students = [10, 20, 30, 50]
    student = {'name': '马云', 'age': 30}
    return render(request, 'App02/var.html', locals())


def handle_filter(request):
    num = 10
    name = '一个字符串'
    return render(request, 'App02/过滤器.html', locals())


def handle_tag(request):
    l1 = [10, 20, 30, 40]
    num = 21
    return render(request, 'App02/tag.html', locals())


def include_div(request):
    return render(request, "App02/list.html")


def handle_url(request):
    return render(request, 'App02/menu.html')


def handle_extends(request):
    return render(request, 'App02/child.html')


def handle_static(request):
    return render(request, 'App02/wenzhang_xinwen.html')
