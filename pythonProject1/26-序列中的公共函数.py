# 公共函数：可以在列表、字典、集合等序列类型中使用
"""
+ :  合并数据(不改源数据)    字符串、列表、元组
* :  复制数据(不改源数据)    字符串、列表、元组
in : 数据是否存在           字符串、列表、元组、字典（键是否存在）、集合
not in : 是否不存在         字符串、列表、元组、字典（键是否不存在）、集合

切片：序列类型[起始索引:结束索引:步长]   适用于字符串、列表、元组（有索引的数据类型）
"""
str1 = 'hello'
str2 = 'world'
print(str1 + str2)

tuple1 = (10,)
print(tuple1 * 5)

set1 = {10, 20, 30}
print(10 in set1)

"""
len() or 容器.__len__():容器中元素个数
del :根据索引下标删除指定函数（元组和字符串的元素不能删除）
max():返回容器中最大值（对字典使用则是键的最大值）
min():返回容器中最小值
range(start, end, step):从start到end的数字，步长step。不含end
enumerate():将一个可遍历的序列组合为一个key:value结构，结合for循环遍历

"""
list1 = [10, 20, 30, 40, 50]
print(list1.__len__())
for key, value in enumerate(list1):
    print(key, value, sep=': ')
    # 自动编号 第一个数据的key是0，第二个是1，以此类推
