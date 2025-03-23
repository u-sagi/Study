"""
1.lambda又称匿名函数
2.函数只有一个返回值，只有一句代码，可用lambda简化
3.能接受任意数量参数(也可以为零)但只能返回一个表达式的值
语法：
lambda 参数列表 : 表达式
"""
def func1(a, b):
    return a + b

print(func1)
print(func1(1, 2))


func2 = lambda a, b: a + b
print(func2)  # 直接输出funcB为内存地址
print(func2(1, 2))

# lambda的参数形式
# 1.无参数
funcA = lambda: 100
print(funcA())
# 2.单参数
funcB = lambda a: a
print(funcB('hello world'))
# 3.默认参数(缺省参数)
funcC = lambda a, b, c=100: a + b + c
print(funcC(10, 10))
# 4.可变参数：*args
funcD = lambda *args: args
print(funcD(10, 20, 30))  # 可变参数以元组形式传入
# 5.可变参数：**kwargs
funcE = lambda **kwargs: kwargs
print(funcE(name='Python', age=20))   # 可变参数以字典形式传入

# 带判断的lambda
funcF = lambda a, b: a if a > b else b
print(funcF(500, 1000))

# 列表数据按字典key值排序
students = [
    {'name': 'Tom', 'age': 27},
    {'name': 'Rose', 'age': 24},
    {'name': 'Jack', 'age': 21}
]
# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)
# 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
