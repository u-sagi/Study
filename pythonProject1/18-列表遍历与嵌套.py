# 列表遍历
list1 = ['Tom', 'Rose', 'Jack', 'Ham']
for i in list1:
    print(i, end=' ')

# 列表嵌套(类似于二维数组或多维数组
list2 = [[], [], []]
list2[0] = [1, 2, 3]
list2[1] = ['a', 'b', 'c']
list2[2] = ['张三', '李四']
print('\n', list2)
# 嵌套列表访问
print(list2[2][1])
# 嵌套列表遍历
for i in list2:
    print(i)