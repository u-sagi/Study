# 使用while循环
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j}', end='\t')
        if j == i:
            print('\n')
        j += 1
    i += 1

# 使用for循环
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={i*j}', end='\t')
    print('\n')