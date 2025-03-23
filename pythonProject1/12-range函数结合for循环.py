# 语法
'''
range()一个可迭代的序列
range(stop) #默认从零开始，“stop”结束
range(start, stop[, step])  # start开始，stop结束，步长为step
start开始，但不包括stop
如：
 range(5)  #默认从0开始，返回0, 1, 2, 3, 4 没有5
 range(0, 5) #等同于range(0, 5, 1) 默认步长为1
'''
for i in range(5):
    print(i)

# 求1~100的和
sum1 = 0
for i in range(101):
    sum1 += i
print(f'1到100的和是{sum1}')

# 1到100中所有偶数的和
sum2 = 0
for i in range(0, 101, 2):
    sum2 += i
print(f'1到100中所有偶数的和是{sum2}')

# 1到100中所有奇数的和
sum3 = 0
for i in range(101):
    if i % 2 == 1:
        sum3 += i
print(f'1到100中所有偶数的和是{sum3}')