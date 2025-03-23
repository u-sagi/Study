# python中的值是靠引用来传递的,若不同变量赋同一个值则地址相同
# 使用函数id()可得到变量对应的值的内存地址，地址相同则变量对应的值一定相同
"""
不可变型：int float bool str tuple
内存空间中的数据不能进行修改，即只能通过开辟新的空间定义新的值
可变类型：list set dict
"""
a = 1  # 开辟内存空间放入值1，将值1赋给a
b = a  # 将a对应的值1赋给b
print(a, b)
print(id(a), id(b))

a = 2  # 开辟新的内存空间放入值2，将值2赋给a
print(a, b)  # 结果为2 1 修改a的值但b仍为1，可知int型数据为不可变型
print(id(a), id(b))
print(id(1))

"""
可变型：列表，字典，集合
数据能进行修改，即可在原内存空间上直接修改原数据
"""
list1 = [10, 20]  # 开辟内存空间放入值[10, 20]
list2 = list1
print(list1, list2)
print(id(list1), id(list2))
list1.append(30)  # 修改值为[10, 20, 30], 但对应的内存地址不变（即没有开辟新的内存地址）
print(list1, list2)  # 结果为[10, 20, 30] [10, 20, 30],可知为可变型
print(id(list1), id(list2))  # 地址与改值之前相同
# 需要注意的是，如果将list1.append(30)语句改为list1 = [10, 20, 30]则结果与不可变型相同


# 不同类型的引用作实参时的情况
def funcA(x):
    print(x, id(x))
    x += x
    print(x, id(x))

aa = 10
bb = [10, 20]
funcA(aa)  # 计算前后aa的id值发生变化，即开辟了新的内存空间存储了新的值
funcA(bb)  # 计算前后bb的id值不变，即在原内存空间上对值做了修改
