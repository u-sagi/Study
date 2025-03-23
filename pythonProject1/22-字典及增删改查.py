# 考虑存储某元素的多个属性时，还要保留整体与部分的联系,考虑字典dict()
"""
特点：数据以键-值对的形式出现{key键名:value值}
        key唯一，数字、字母都可
(考虑到其他序列用索引读取时，可能因修改而导致索引对应的数据发生变化,而字典是一一对应)
语法：字典名称 = {属性1, 属性2, 属性3, ...}
"""
dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male'}

# 增加/修改字典数据
'''
字典名称[key] = value
(若这个key在字典中没有,则增加该数据，有则修改这个key对应的值)
字典也是【可变类型】，参考17-列表
'''
person = {}  # 定义空字典
person['name'] = 'Ella'  # 增加操作
person['age'] = 20
person['gender'] = 'female'
print(person)

# 删除字典数据
'''
--- del 字典名称[key]
--- 字典名称.pop(key)
--- clear():清空字典
'''
del person['gender']
print(person)

# 查找字典数据
'''
直接打印key对应的值报错就代表没有数据
get(key, 默认值):根据key获得value,
若key不存在则返回默认值，默认返回none
keys():返回字典中所有key，返回为dict_keys数据类型(可遍历)
values():返回字典中所有value，返回为dict_values数据类型(可遍历)
items():获取字典全部数据,以元组(key, value)形式输出,返回为dict_items数据类型(可遍历)
for循环遍历字典数据
'''
print(person['age'])

name = person.get('name')
age = person.get('age')
gender = person.get('gender', 'male')  # 若没有对应key信息，则gender = male
print(f'姓名：{name}  年龄：{age}')

print(person.keys())
print(person.values())
print(person.items())

for key1, value1 in person.items():
    print(f'{key1}:{value1}')
