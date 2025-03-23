"""
1.函数内部对变量的赋值无法改变全局变量
2.在函数内部的变量前加上global可定义成全局变量
"""
# 定义全局变量，函数内外都能访问
str1 = 4

# 定义funcA函数,试图修改str1变量为5
def funcA(str1):
    str1 = 5
    return str1

# 定义funcB函数,声明str1为全局变量后修改为5
def funcB():
    global str1
    str1 = 5

funcA(str1)
print(str1)  # 结果仍然为4
funcB()
print(str1)  # 结果为5
