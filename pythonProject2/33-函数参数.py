# 关键字传参
"""
1.通过‘键＝值’的方式传入参数，这种方法无需遵循函数形参的顺序
2.若只有部分参数通过关键字传参，则应先写按位置传参的，再写按关键词传参的
"""


def funcA(name: str, age: int, gender: str):
    print(f'姓名：{name},年龄：{age},性别：{gender}')


funcA('张三', gender='男', age=20)  # 姓名按位置传参，性别年龄按关键字传参

# 缺省参数
"""
1.缺省参数写在最后面
2.调用函数时给缺省参数传参则修改默认值，否则使用默认值
"""


def funcB(name, age, gender='男'):
    print(f'姓名：{name},年龄：{age},性别：{gender}')


funcB('李四', 21)

# 不定长参数(可变参数)
# 1.不确定调用时会传递多少个参数
# 2.分为包裹位置传递和包裹关键字传递两种方式
# 3.以上两种方式都是将数据进行组包的过程（即输入零散数据返回整体数据）
"""
不定长位置参数 包裹位置传递：
 ①调用时所有传进的参数按传进顺序合并成元组形式被args变量收集
格式：
def funcA(*args)：
    ...
    
不定长关键字参数 包裹关键字传递：
 ①调用时所有传进的参数按字典形式被kwargs变量收集
格式：
def funcA(**kwargs):
    ...
    
"""


def funcC(*args):
    print(args)

funcC('Tom', 20)


def funcD(**kwargs):
    print(kwargs)

funcD(name='Tom', age=20)


def func1(func):
    def func2():
        print('登录验证成功')
        func()
    return func2

@func1
def show_user():
    print('展示用户信息')



