# if判断语句
# 通过删去缩进来跳出判断
'''
if 条件判断：
   执行代码
else:
   执行代码
  # 这里留一个空行与其他代码隔开，增加可读性
其他代码...
'''

'''
if 判断语句1:
    执行代码1
elif 判断语句2:
    执行代码2
else:
    执行代码3
'''
age = int(input('请输入年龄：'))
if age < 0:
    print(f'输入有误，请重新尝试。')
elif age < 18:
    print(f'{age}岁不是合法工作年龄。')
elif age < 60:
    print(f'{age}岁是合法工作年龄。')
else:
    print(f'{age}岁是法定退休年龄。')
# python中可以写 “18 <= age <= 60”这样的判断语句
