# 文件备份
"""
1.接收输入的文件名(筛选无效文件名)
2.规划备份文件名
3.数据写入备份文件
4.关闭文件
"""
# 文件名的提取
old_name = input('请输入要备份的文件名：')
index = old_name.rfind('.')  # 提取文件后缀点的位置下标
if index > 0:  # 防止出现.txt这类无效输入
    tempname = old_name[:index]  # 提取去除后缀的文件名
postfix = old_name[index:]  # 提取后缀
new_name = tempname + '[备份]' + postfix

# 打开原始文件与备份文件
old_file = open(old_name, 'rb')  # 二进制只读模式打开原始文件
new_file = open(new_name, 'wb')  # 二进制写入模式创建备份文件

# 由于无法预知待备份文件的大小，因此循环读取文件，备份写入
while True:
    content = old_file.read(1024)  # 一次循环读取1024字节数据
    if len(content) == 0:  # 无可读取内容则退出循环
        break
    new_file.write(content)  # 写入备份内容

new_file.close()
old_file.close()
print(f'文件<{old_name}>备份成功，备份文件名为<{new_name}>。')