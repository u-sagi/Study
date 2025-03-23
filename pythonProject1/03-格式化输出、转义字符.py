# 用百分号进行格式化输出
m = 'milk'
c = 'coke'
print('m的值是%s%%，c的值是%s。' % (m, c))  # 如果要输出%则需要转义，即%%
'''
%s 输出字符串
%d 输出带符号的十进制整数
  %06d 位数不足6位的用0进行前补齐
  id = 1
  print('id = %06d' % (id))
%f 小数类型
   %.2f 保留两位小数
'''

# format方法格式化输出
name = '张三'
mobile = 123456
print('姓名：{}\n联系方式：{}'.format(name, mobile))
# format简写形式
print(f'姓名：{name}\n联系方式：{mobile}')
# format方法下保留小数位数
num = 3.1415926
print(f'{num:.4f}')  # :.2f意为保留两位小数，遵循四舍五入原则
print(f'姓名：{name}')

# 转义字符
'''
\t：制表符(四个空格)
\n：换行符
'''
# 每一个print()执行完毕后会自动输出一个换行符如不需要换行可以添加一个end参数
print('*', end='')
print('*', end='')
print('*', end='')