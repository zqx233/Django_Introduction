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
    return render(request, 'example.html', context={'name':'admin'})
