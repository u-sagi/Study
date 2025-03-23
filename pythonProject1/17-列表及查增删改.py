# 列表list()：可以一次存储多个不同类型的数据，在其他语言中又被称为数组
"""
语法：
列表名称 = [数据1, 数据2, ...]
"""
import collections
c = collections.Counter([1, 2, 3, 4, 5, 6])
print(c.keys())
list1 = ['a', 'b', 'c', 'd']
print(list1)  # 打印结果为['a', 'b', 'c', 'd']
list1 = list1[::-1]
print(list1)
# 查找列表中数据
# 可直接根据数据的索引下标查找
print(list1[0])
print(list1[1:])
print(list1[:2])
'''
index():返回指定数据所在下标
count():返回指定数据在当前列表出现次数(根据这个函数可看出,列表中数据可有相同的)
in:判断指定数据是否在列表中，返回值为bool值
not in:与上面相反
'''
print(list1.index('d'))
print('a' in list1)

# 增加列表的数据
# 列表为【可变】类型数据，即可以通过函数修改列表本身
# 对比之前字符串也有的修改操作,当打印原字符串时可知操作对其本身并无影响
'''
append(需添加的数据1):列表尾部添加数据
extend():可在列表尾部添加一系列数据,通常用来合并列表
insert():在指定位置(元素索引下标)增加元素
'''
list2 = ['book', 'pen', 'eraser', 'pencil-box']
list2.append('ruler')
print(list2)
list2_1 = ['bag']
list2.extend(list2_1)
print(list2)  # 如果直接写‘bag’,会以'b''a''g'这样的形式录入,因此采用列表合并的方法
list2.insert(1, 'tips')
print(list2)

# 删除列表数据
'''
del 列表名称[索引下标]:删除列表中某数据
pop():删除指定下标的数据(默认删除最后一个)，返回结果为待删除的数据
remove():直接根据数据删除第一个数据
clear():清空列表
'''
list3 = ['Tom', 'Rose', 'Jack', 'Jack', 'Ham']
del list3[1]
print(list3.pop())
list3.remove('Jack')
print(list3)
list3.clear()
print(list3)

# 修改列表数据
'''
列表名称[索引1], 列表名称[索引2] = 修改后的值1, 修改后的值2
reverse():倒叙排列列表
sort():进行排序(升序，降序)
copy():进行拷贝，对新列表的修改就不回影响原列表
'''
list4 = [1, 2, 3, 4, 5, 7]
list4[5] = 6
print(list4)
list4.reverse()
print(list4)
list4.sort()  # 升序排列
# list4.sort(reverse=True)  # 降序排列
print(list4)
list4_1 = list4.copy()  # 复制列表，对新列表的修改不会影响原列表的值
print(list4_1)
