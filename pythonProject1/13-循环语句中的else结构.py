"""
循环结构中有的else结构：
当循环结构正常结束，才会执行else语句内部的代码。
而如遇到break等不正常结束的情况时，else语句内部代码不会执行。
continue时没有影响。
"""
# while循环
sumresult = 0
i = 1
while i <= 5:
    sumresult += i
    if i == 4:
        break
    i += 1
    print(sumresult)
else:
    print('程序执行正常。')

# for循环
sumresult = 0
for i in range(1, 6):
    sumresult += i
    if i == 6:
        break
    print(sumresult)
else:
    print('程序执行正常。')
