import pandas
# 异常捕获
'''
try:
    可能出现报错的代码
except:
    出现异常后，执行的代码
1.将可能异常的代码放入try块中，如有异常则执行except块中的代码
2.如果存在多个异常，则第一个异常后续的代码不会执行，直接跳入except中
'''

# 捕获指定类型的异常
'''
try:
    代码
except (异常类型1,异常类型2):
    代码
except (异常类型3, 异常类型4):
    代码
except Exception:  # Exception是所有异常类型的父类，用于捕获未知异常
    代码
else:
    不出现异常执行的代码
finally:
    必定会执行的代码，哪怕报错也会执行
1.展示异常信息：except 异常类型 as 变量:...  然后打印变量就能得到异常信息
'''

try:
    # print(a)
    print(1/0)
except ZeroDivisionError as error:
    print('零不能作为分母。', error)
except NameError as error:
    print('出现了NameError异常。', error)
except Exception as error:
    print("出现了未知异常。", error)

# 自定义异常
"""
1.继承Exception
2.继承后要重写Exception方法
"""


class PasswordError(Exception):
    error_num = 0  # 类属性，密码错误次数

    def __init__(self, str):
        super().__init__(str)  # 实现Exception的初始方法
        PasswordError.error_num += 1

try:
    password = input('请输入密码：')
    if len(password) < 6:
        raise PasswordError('密码不足六位。')  # raise抛出异常

    if password != '888888':
        raise PasswordError("密码错误，请重试。")

    if PasswordError.error_num >= 3:
        raise PasswordError("错误次数过多，请稍后再试。")
except PasswordError as error:
    print(error)
