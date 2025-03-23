"""算术运算符"""
import math
# 加：+  减：-  乘：*  除：/  取余：%
# 整除符号：//
num1 = 9//4  # 等于2
print(num1)
print('-' * 20)  # 输出20个“-”符号
# 幂指数：**
num2 = 2 ** 4  # 2的4次方等于16
print(num2)

# 多个变量同时赋值
a, b, c = 10, 20, 'hello world'
d = e = 40
# 复合赋值运算符
a += b  # a = a + b
d **= e  # d = d ** e
a *= 1 + 2  # ！！先算等号右边的再算乘等于符号
print(a)
"""逻辑运算符：and or not"""
l1 = 1
l2 = 2
l3 = 3
print((l1 > l2) and (l2 > l3))  # 输出False
print((l1 < l2) or (l2 > l3))  # 输出True
print(not (l1 > l2))  # 输出True
# 0、空字符串和None看成False，其他数值和非空字符串都看成True
print(5 or 6)  # 从左到右“5”已经让式子为True了，所以后面不用看了，输出5
print(0 or 1)  # “1”让式子为True，输出1
print(0 and 1)  # “0”已经让式子变为False了，后面不用看，输出0
print(5 and 6)  # 从左到右读到“6”才能确定整个为True，输出6

"""
三目运算符
 就是简化的 if...else...语句
语法：语句1 if 条件判断 else 语句2
完整版：if 条件判断:
          语句1
       else:
          语句2
"""
num = int(input('输入一个数字：'))
max = 2 if 2 > num else num
print(f'{num}与2相比，较大的数字是{max}')

