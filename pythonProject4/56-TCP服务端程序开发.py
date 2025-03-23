import socket
import threading
"""
开发流程：
1.创建服务器连接对象
2.绑定IP地址和端口
3.指定监听的数量
4.等待客户端连接
5.接收客户端的数据
6.返回数据
7.关闭服务端
"""


# 封装处理客户端数据方法
def client_data(client_sock: socket):
    while True:  # 循环语句能让服务端不断处理同一个客户端的数据
        '''5.接收客户端数据'''
        recv_data = client_sock.recv(1024)
        str_data = recv_data.decode()
        print(f'接收到客户端的数据：{str_data}')

        '''6.返回数据'''
        data = 'hello client'
        client_sock.send(data.encode())


'''1.创建服务器对象'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ipconfig 查看IPv4地址
'''2.绑定IP地址和端口'''
server.bind(('192.168.88.8', 8080))

'''3.设置监听的数量'''
server.listen(5)

# 让while True包括4~6步，保持服务端持续运行
while True:
    # 接收过来的是客户端对象和客户端地址
    '''4.等待客户端连接'''
    client_sock, addr = server.accept()

    # 每次接收到数据，都会交给线程进行处理
    t = threading.Thread(target=client_data, args=(client_sock,))
    t.start()

'''7.关闭服务端'''
server.close()
