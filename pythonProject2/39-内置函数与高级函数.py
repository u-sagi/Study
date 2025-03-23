import functools
# 内置函数
'''
1.abs()求绝对值
2.round()四舍五入
'''

# 高阶函数
'''
1.把函数作为参数传入
2.是函数式编程的体现
'''
def funcA(a, b, f):
    return f(a)+f(b)

print(funcA(2.4, 2.9, round))  # 将round作为参数传入

# 内置高阶函数
"""
1.map(func, lst) 将传入的函数func作用到lst变量的每个元素中，并将结果组成新的迭代器返回，
  可用list()转列表
2.reduce(func,lst) 每次func计算的结果继续与lst下一元素做累计计算，其中func须有两个参数
3.filter(func, lst) 筛选出lst中符合func的元素，过滤不符合条件的元素, 返回一个filter对象,
  可用list()转列表
"""
list1 = [1, 2, 3, 4, 5]
# map() 求列表中每个数字的平方
result1 = map(lambda x: x ** 2, list1)
print(list(result1))  # 直接打印为map内存地址，需用list()转为列表格式
# reduce() 计算list1各个数累加和
result2 = functools.reduce(lambda a, b: a + b, list1)  # 两个参数a,b
print(result2)
# filter() 过滤list1中的所有偶数
result3 = filter(lambda x: x % 2 == 1, list1)  # 匿名函数返回的是一个判断语句x%2==1
print(list(result3))