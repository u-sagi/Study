# 交换变量值
m = 'milk'
c = 'coke'
t = c
c = m
m = t
print(m)  # 调用变量时不用加引号，只有是字符串时才加
print(c)

# 数据类型
'''
数 值：int（整数） float（浮点数）
布尔型：True False （首字母必须大写！）
str字符串
list列表
  a = [10, 20, 30, 40]
tuple元组
  b = (10, 20, 30, 40)
set集合:去重
  c = {10, 20, 30, 40}
dict字典
  d = {'name':'张三', 'age':18}
'''

# 判断变量类型
print(type(m))  # 输出变量m的类型
print(isinstance(m, str))  # 判断是否为str类型 输出值为布尔类型

