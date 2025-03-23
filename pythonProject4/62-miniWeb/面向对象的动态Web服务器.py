import socket
import threading
import json
import pymysql


class WebServer(object):
    # 初始化
    def __init__(self, ip: str, port: int):
        # 创建socket对象
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定ip和端口
        self.server.bind((ip, port))
        # 监听数量
        self.server.listen(5)
        # 路径的路由列表
        self.url_list = [
            ('/', self.index),
            ('/detail', self.detail)
        ]

    # 路径为'/'时执行的函数
    def index(self, url_dict: dict) -> list:
        sql_str = 'select * from employees limit 10'
        return self.queryDB(sql_str)

    # 路径为'/detail?...'时执行的函数
    def detail(self, url_dict: dict) -> list:
        if len(url_dict) > 1:
            sql_str = 'select * from employees where ' + url_dict['url_query']
            print(sql_str)
            queryRes_list = self.queryDB(sql_str)
        else:
            queryRes_list = []
        return queryRes_list

    # 路径处理判断函数
    def url_route(self, url_dict: dict) -> list:
        for url, func in self.url_list:
            if url_dict['url_path'] == url:
                return func(url_dict)
                break
        else:
            print("路径查找失败。")
            return ['fail']

    # 连接数据库并执行查询语句，列表形式返回查询数据
    def queryDB(self, sql_str: str) -> list:
        # 配置mysql连接信息
        db = pymysql.connect(user='root', password='1234', host='192.168.88.2', database='employees')
        # 创建连接对象（游标）
        cursor = db.cursor()
        # 执行sql查询语句
        try:
            cursor.execute(sql_str)
        except Exception as e:
            return [f'{sql_str}\n{e}']
        # 获取查询数据(元组类型)
        res_data = cursor.fetchall()
        # 将每一条数据存入列表中
        data_list = []
        for i in res_data:
            data_list.append({
                "emp_no": i[0],
                # "birth_date": i[1],
                "first_name": i[2],
                "last_name": i[3]
            })
        return data_list

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
            # 基于问号进行路径分割
            url_split = url_path.split('?')
            url_dict = {
                "url_path": url_split[0],
                "url_query": url_split[1] if len(url_split) > 1 else ''
            }
            # 根据请求路径返回查询数据
            queryRes_list = self.url_route(url_dict)
            # 将保存了字典数据的列表转为json数据  第二个参数保证能解析汉字不乱码
            send_data = json.dumps(queryRes_list)
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

    # 启动服务器
    def start(self):
        while True:
            # 等待连接
            client_socket, addr = self.server.accept()
            # 创建线程处理客户端数据
            t = threading.Thread(target=self.client_request, args=(client_socket,))
            t.start()

    # 关闭服务器
    def close(self):
        self.server.close()


server = WebServer('127.0.0.1', 9000)
server.start()
# 关闭服务器
server.close()
