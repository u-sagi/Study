# 多进程模块
import multiprocessing
import os

def login(name: str, password: str):
    # 获取运行的进程的名称
    print(f'当前进程名称：{multiprocessing.current_process().name}')
    # 获取当前进程的编号
    print('子进程：', os.getpid())
    # 获取父进程编号
    print('父进程：', os.getppid())
    print(f'姓名：{name}')
    print(f'密码：{password}')
    print('登录成功。')

# group=None            指定分组，默认为空
# target=None           指定函数名
# name=None             指定进程名称
# args=(), kwargs={}    以元组/字典方式给函数传递参数
# daemon=None           指定守护进程
if __name__ == '__main__':  # 不写这个会报错，在其他文件执行时，系统防止该文件多次执行浪费资源
    # 创建进程
    p1 = multiprocessing.Process(target=login, args=('小小', '123123'), name='p1')
    p2 = multiprocessing.Process(target=login, kwargs={'name': '两两', 'password': '123123'}, name='p2')
    # 运行进程对应的函数逻辑
    p1.start()
    p2.start()
    # 执行当前文件就会有一个进程，其中的进程就是子进程
    # 获取进程编号
    print('主进程：', os.getpid())

# 让进程按顺序执行：join方法
'''
p1.start()
p1.join()  # p1执行完毕后再执行其他进程
p2.start()
p2.join()   # p2执行完毕后再执行其他进程
...
'''


