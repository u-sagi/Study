# 导入网络开发工具（模块）
import socket
"""
开发流程：
1.创建socket对象
2.连接服务器
3.发送数据
4.接收服务器返回的数据
5.关闭客户端
"""

# socket.AF_INET     指定IP地址为IPv4形式
# socket.SOCK_STREAM 指定通信方式为TCP协议
'''1.创建对象'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ipconfig 查看IPv4地址
'''2.连接服务器'''
client.connect(('192.168.88.8', 8080))

# b'字符串'是直接按照bytes类型传输数据
# 或者 字符串.encode() 将字符串转为bytes
'''3.发送数据'''
data = 'hello server'
client.send(data.encode())

# client.recv(1024) 规定每次接收的数据大小
# 将bytes类型转为str .decode()
'''4.接受服务端返回的数据'''
recv_data = client.recv(1024)
str_data = recv_data.decode()
print(f'接收到服务端的数据：{str_data}')

'''5.关闭客户端'''
client.close()
