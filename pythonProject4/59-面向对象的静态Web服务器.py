import socket
import threading


class WebServer(object):
    # 初始化
    def __init__(self, ip: str, port: int):
        # 创建socket对象
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定ip和端口
        self.server.bind((ip, port))
        # 监听数量
        self.server.listen(5)

    # 处理客户端请求
    def client_request(self, client_socket):
        while True:
            # 接收客户端数据
            recv_data = client_socket.recv(1024)
            str_data = recv_data.decode()

            # 浏览器有可能发送空数据，为防止后续切割空数据导致出错，需要加上这个判断
            if len(recv_data) == 0:
                return

            # 根据请求报文中的路径，返回指定页面
            # 切割数据
            data_list = str_data.split('\r\n')
            # 请求行
            request_line = data_list[0].split(' ')
            # 请求的资源路径
            url_path = request_line[1]
            # 返回前端文件数据给客户端
            if url_path == '/':
                f = open('58-静态Web服务器/index.html', 'r', encoding='utf-8')
            elif url_path == '/login':
                f = open('58-静态Web服务器/login.html', 'r', encoding='utf-8')
            else:
                f = open('58-静态Web服务器/error.html', 'r', encoding='utf-8')
            send_data = f.read()
            f.close()

            # 构建响应报文数据
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应头
            response_header = 'Server:python\r\nContent-type:text/html\r\n\r\n'
            # 响应体
            response_body = send_data
            # 拼接三部分数据，构成完整的响应报文
            response_data = response_line + response_header + response_body
            client_socket.send(response_data.encode())

    # 关闭服务器
    def close(self):
        self.server.close()

    # 启动服务器
    def start(self):
        while True:
            # 等待连接
            client_socket, addr = self.server.accept()
            # 创建线程处理客户端数据
            t = threading.Thread(target=self.client_request, args=(client_socket,))
            t.start()


server = WebServer('127.0.0.1', 9000)
server.start()
# 关闭服务器
server.close()
