for i in range(6):
    print(' ' * (5 - i), end='')  # end用来删除自动形成的换行
    print('*' * (2 * i - 1), end='')
    print(' ' * (5 - i))

# 反色等腰三角形
str1 = ' '
print('\n')
for i in range(7):
    print(f"{str1.center(15, '*')}")
    str1 = str1 + '  '
