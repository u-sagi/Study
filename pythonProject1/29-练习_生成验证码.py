import random
str1 = '23456789abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
# 删除数字0,1 字母o,l,O 因为不容易区分
code = ''
for i in range(4):
    index = random.randint(0, len(str1)-1)
    code = code + str1[index]
print(code)


