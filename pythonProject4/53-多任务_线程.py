# 导入线程模块
import threading

sumresult = 0
def func1():
    print(f'当前线程名称：{threading.current_thread().name}')
    for i in range(0, 1000000):
        global sumresult
        sumresult += 1
    print(f'函数1累加结果：{sumresult}')

def func2():
    print(f'当前线程名称：{threading.current_thread().name}')
    for i in range(0, 1000000):
        global sumresult
        sumresult += 1
    print(f'函数2累加结果：{sumresult}')

# group=None            指定分组，默认为空
# target=None           指定函数名
# name=None             指定线程名称
# args=(), kwargs={}    以元组/字典方式给函数传递参数
# daemon=None           指定守护线程
if __name__ == '__main__':
    # 创建进程

    t1 = threading.Thread(target=func1, name='t1')
    t2 = threading.Thread(target=func2, name='t2')
    t1.start()
    t2.start()
    print(f'主线程累加结果：{sumresult}')
