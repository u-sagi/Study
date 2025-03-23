# 闭包
"""
1.概念：在函数嵌套的前提下，内部函数调用外部函数变量/传参，且外部函数return内部函数名，称
        内部函数为【闭包】。
"""

def func1(num1):
    print(f'第一个值为{num1}')
    def func2(num2):
        print(f'第二个值为{num2}, 求和为{num1 + num2}')
    return func2

f = func1(10)  # 此时内部函数func2并没有被调用，且num1的值没有被释放
f(20)


# 修饰器
"""
1.在不改变已有函数【代码】和【调用方式】的情况下添加额外的功能，本质是闭包函数。
"""

def validate(func):
    def f(*args, **kwargs):
        print('验证登录信息成功。')
        func(*args, **kwargs)
    return f

@validate
def show_user(name):
    print(f'姓名：{name}')

@validate
def buy():
    print('商品购买')

show_user('小明')  # show_user()的源代码和调用都没有改变
buy()