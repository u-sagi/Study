# 推导式:实质上是简化代码的一个方法,常用于序列数据有一定规律时。
# 列表推导式
"""
列表推导式
语法：
列表名 = [表达式 for 变量 in 列表]
   通过 '变量' 遍历 '列表' 依次带入'表达式'中并将'表达式'依次导入列表
列表名 = [表达式 for 变量 in 列表 for 变量 in 列表]
   两个for循环为嵌套关系，第一个是外层，第二个是内层
列表名 = [表达式 for 变量 in 列表 if 条件]
"""
# 普通方法
# 创建一个包含0-9整数的列表
list1 = []
for i in range(0, 10):
    list1.append(i)
print(list1)

# 列表推导式
# 创建包含0-9中所有整数的平方的列表
list2 = [i**2 for i in range(0, 10)]
# 第一个i**2这里可以写成表达式，这个值会依次放入到列表中
print(list2)
# 创建包含0-9中所有偶数的列表
list3 = [i for i in range(0, 10) if i % 2 == 0]
print(list3)
# 嵌套for循环列表推导式
list4 = [(i, j) for i in range(1, 3) for j in range(0, 3)]
print(list4)

# 字典推导式
"""
字典推导式
语法：
字典名 = {key:value for key,value in 序列}
"""
# 普通方法
# 创建字典，key是1-5的整数，value是对应key的平方
dict1 = {}
for i in range(1, 6):
    dict1[i] = i**2
print(dict1)

# 字典推导式
dict2 = {i: i**2 for i in range(1, 6)}
print(dict2)
# 两个列表合并为字典
list2_1 = ['name', 'age']
list2_2 = ['ella', 20]
dict3 = {list2_1[i]: list2_2[i] for i in range(len(list2_1))}
print(dict3)
# 提取字典中value大于等于200的数据
dict4_1 = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'ACER': 99}
dict4_2 = {key: value for key, value in dict4_1.items() if value >= 200}
print(dict4_2)

# 集合推导式
"""
集合推导式
语法：
集合名 = {表达式 for 临时变量 in 序列}
"""
# 创建一个集合，数据为list4_1的数据的平方
list4_1 = [1, 1, 2]
set3 = {i**2 for i in list4_1}  # 自动去重
print(set3)
