import os

# 文件操作
'''
①os.rename(原文件名, 新文件名)      重命名
  os.remane(文件名1, 路径/文件名1)   移动到指定路径下
②os.remove(文件名)                 删除文件
文件名皆可带路径
'''

# 文件夹操作
'''
①os.mkdir(文件夹名)               创建文件夹，如已存在则会报错
②os.rmdir(文件夹名)               删除文件夹
③os.rename(原文件夹名, 新文件夹名)  重命名
④os.getcwd()                     获取当前目录(文件夹名)
⑤os.chdir(目录)                   修改默认目录
⑥os.listdir(目录)                 获取目录列表(文件夹内的所有文件)，以列表形式输出
'''
print(os.getcwd())
print(os.listdir())
