# 数据类型转换方法
"""
 int(x)  # 把x转换成整数
 float(x)  # 把x转换成浮点数
 str(x)  # 把x转换成字符串
 eval(x)  #把字符串x转化为原数据类型
   str1 = '10'  eval(str1) 转换成了int类型
   str2 = '10.1'  eval(str2) 转换成了float类型
"""
# 实现超市的收银系统
name = input('请输入你要买的商品名称：')
id = input('请输入商品编号：')
price = float(input('请输入商品价格：'))
num = eval(input('请输入你要买的个数：'))
print(f'您购买了{num}瓶{name}，该商品编号为{id},价格为{num * price:.2f}元，欢迎下次光临！')
# {num * price:.2f}中：.2f指保留两位小数
