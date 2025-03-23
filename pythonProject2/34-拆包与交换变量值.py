# 拆包元组
def funcA(*args):
    return args


tuple1 = funcA(100, 200)
print(type(funcA(100, 200)))
print(tuple1[0], tuple1[1])


# 拆包字典
def funcB(**kwargs):
    return kwargs


dict1 = funcB(name='Tom', age=20)
key1, key2 = dict1  # 取出的是key值
print(type(dict1))
print(key1, key2)
print(dict1[key1], dict1[key2])

# 交换变量
a, b = 1, 2
a, b = b, a
print(a, b)

c, d, e = 1, 2, 3
c, d, e = e, c, d
print(c, d, e)
