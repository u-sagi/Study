"""
将一个进程的执行结果写入文件，另一个进程读取该文件
以文件作为桥梁传递数据
"""
import multiprocessing

data_list = []
def write_data():
    for i in range(0, 50):
        data_list.append(i)
    f = open('commu.txt', 'w')
    f.write(str(data_list))
    f.close()

def read_data():
    f = open('commu.txt', 'r')
    print(f'读取到的数据：{f.read()}')
    f.close()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)
    p1.start()
    p1.join()  # 先等数据读完
    p2.start()


