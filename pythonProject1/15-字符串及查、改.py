"""三引号可多行输入字符串"""
str1 = '''hello
world'''  # 输出结果也会换行
print(str1)
# 若字符串中存在单引号，则使用双引号，反之亦然。
# 如：str = "I'm Lee"

# python字符串属于序列结构，其中的字符可根据索引下标进行快速查找
'''len():求字符串长度'''
str2 = 'hello world'
print(str2[0])
print(str2[2])
print(f'字符串长度为{len(str2)}')  # 求字符串长度

# 字符串切片：截取字符串的一部分。字符串、列表、元组都支持切片。
# 语法：序列名称[开始位置下标:结束位置下标:步长]
# 步长可正可负，负数则代表从右向左
print(str2[:4])  # 从头开始，前四位
print(str2[4:])  # 从下标对应字符开始，到结尾
print(str2[-1:-3:-1])  # 字符串翻转

# 字符串查找
'''
find():查找某子串是否在某字符串中，有则返回第一个对应下标位置，否则返回-1
index():功能同上，但当子串不存在时会报错
rfind():从字符串右边开始查找，其余与find()一致
rindex():同上，其余与index()一致
count(子串,[开始位置下标,结束下标]):返回子串出现的次数，可指定在哪个范围内查找
'''
print(str2.find('world'))
print(str2.count('l'))

# 字符串修改
'''
字符串是【不可变】类型，修改不会改变原有字符串
replace(要替换内容,替换后内容[,替换次数])  默认全部替换
capitalize():字符串的首字母大写,其余位置不是小写的变成小写
title():字符串所有单词首字母大写,以"空格""_"等区分单词
可配合replace再去掉这些特殊分隔符
upper():全部大写
lower():全部小写

strip():删除字符串两边的空白字符
lstrip():删除字符串左边的空白字符
rstrip():删除字符串右边的空白字符

ljust(占用长度,填充字符):左对齐，剩余空间由填充字符填充
rjust(占用长度,填充字符):右对齐，剩余空间由填充字符填充
center(占用长度,填充字符):居中对齐，剩余空间由填充字符填充
'''
str3 = "hello world"
print(str3.replace('hello', 'hi', 2))
print(str3)  # replace之后str3并没有变

print(str3.capitalize())
print(str3.title().replace(' ', ''))  # 大写单词首字母，再去掉单词间的空格

print(str3.center(30, '-'))

# 字符串切割/合并
'''
split():对某些有规律的字符串，可将某一符号作为切割符号对字符串切割
返回一个list()列表结构
分隔符.join(列表1): 根据分隔符合并列表字符串，注意列表中元素须全都是字符串类型，否则报错
--- '-'.join(list1)
'''
str4 = "a-b-c-d"
print(str4.split('-'))
print(str4)  # 虽是切割,但str4并没有变

# 字符串判断 返回类型为bool类型
'''
startswith():判断字符串是否以指定子串开头
endswith():判断字符串是否以指定子串结尾
isalpha():判断字符串是否全为字母，默认将中文也视为字母
分开看的方法：字符串.encode('utf-8').isalpha()
isdigit() or isnumerical():判断字符串是否全为数字，后者会判断中文/罗马/阿拉伯的数字，如叁④亖等
isalnum():判断字符串是否由字母+数字组成(只由数字或字母组成也是True)
isspace():判断字符串是否只包含空白，是则True(前提是至少包含一个字符)
'''
str5 = 'abcd'
print(str5.isalnum())