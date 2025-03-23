"""
list():转换为列表
tuple():转换为元组
set():转换为集合
"""

# 元组
tuple1 = (10, 20, 30)
print(list(tuple1))
print(set(tuple1))

# 集合
set1 = {1, 2, 3}
print(list(set1))
print(tuple(set1))

# 字典:转换后只会保留key，value会被舍弃
dict1 = {'name': 'ella', 'age': 18}
print(list(dict1))
print(tuple(dict1))
