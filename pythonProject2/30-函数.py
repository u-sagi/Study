# 函数定义
'''
def 函数名(参数)：
    """函数的说明文档"""
    函数体
    return 返回值

调用：
函数名(参数)
'''

"""
1.如果存在多个return,只会返回第一个return,
  程序会认为函数执行完毕,后续return不会被执行
2.一般一个函数调用只会返回一个结果,可通过返回
  元组的形式返回多个值
3.return a,b 这种形式,默认返回的是元组类型数据
4.函数说明文档，用三引号定义在函数的第一行，起着类似注释的作用。
  之后可通过help(函数名)的方式调出函数说明文档。
5.函数定义后，内部代码直到调用时才会执行
"""


# 封装一个函数用于生成指定长度的验证码
def generate_code(num: int) -> str:
    """generate_code()主要用于生成指定长度的验证码,参数为长度"""
    import random
    str1 = '23456789abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
    code = ''
    for i in range(num):
        index = random.randint(0, len(str1) - 1)
        code += str1[index]
    return code


help(generate_code)  # 查看函数作用
print(generate_code(5))  # 调用
