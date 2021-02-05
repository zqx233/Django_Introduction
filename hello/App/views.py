from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def index(request):
    # return HttpResponse("Hello world")
    return render(request, "Appindex.html", context={"title": 'Django', "name": '中国'})


def get_phone(request, tel):
    # request常用属性
    # get传参的获取
    print(request.GET)  # GET quersetDict，不能修改
    # 获取单一值
    print(request.GET.get('username'))
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

    return HttpResponse(tel)


def handle_response(request):
    # res = HttpResponse("响应对象")
    # res.content_type = "text/html"
    # res.status_code = 400 # 人为设置状态码
    # return res

    # render返回响应对象
    # res = render(request, 'Appindex.html')
    # return res

    # jsonresponse 可以返回json字符串，一般时候可以把字典，列表转换为json返回给前端，字典，列表只能包含内置类型
    # return JsonResponse({'name': 'tom'})
    # 如果参数不是字典，必须把safe设置为false
    return JsonResponse([1, 2, 3, 4, 5], safe=False)


def handle_redirect(request):
    # 重定向到指定路由地址，参数就是路由
    # return HttpResponseRedirect('/app/')
    # 可用缩写
    # return redirect('/app/')
    # 应用外跳转，参数为绝对地址
    # return redirect('https://www.baidu.com')
    # 带参数重定向
    # return redirect('/app/tel/{}/'.format('12345678'))
    # return redirect('/app/tel/12345678')

    # 反向定位：由应用的命名空间：name来确定路由，应用命空间见url.py
    # return redirect(reverse('App:index'))  # 不带参数
    # 带参数，如果参数有名字，必须使用关键字传参的方式
    # return redirect(reverse('App:tel', kwargs={'tel': '12345678'}))
    # 没名字，用args传参，可以时列表或元组
    return redirect(reverse('App:tel', args=('12345678',)))  # 元组只有一个元素的话后面要加，
