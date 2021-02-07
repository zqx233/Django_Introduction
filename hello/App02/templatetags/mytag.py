from django import template

# 建立模板对象
register = template.Library()


# name表示在模板中使用的过滤器名称
@register.filter(name='sub1')
def sub(value):  # 参数必须是1~2个
    return value - 1
