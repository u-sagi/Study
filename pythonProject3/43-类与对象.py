# 类与对象的关系
"""
用类创建一个对象/用类实例化一个对象
"""

# 类
'''
①类是对一系列相同’特征‘和’行为‘的事物的统称，是抽象的概念。
  特征即是属性(变量)，行为即是方法(函数)
②经典类语法：
  class 类名:  # 类名满足命名规则，且遵循【大驼峰命名】习惯
    代码...
  新式类语法：
  class 类名(父类名):
    代码...
③一个类可创建多个对象，但对象(self)内存地址不同
'''
# 对象 是类创建出来的真实存在的事物
'''
①先有类，后有对象
②创建对象：对象名 = 类名()
'''
# self 指的是调用该函数的对象


class Washer:
    def wash(self):  # 定义在类里的方法(函数)，又称实例方法/对象方法
        print('洗衣服')
        print(self)  # 默认打印对象内存地址，定义了__str__()方法则打印该方法中return的数据

    def __init__(self):  # 初始化对象
        self.width = 400
        self.height = 500

    def __int__(self, width, height):  # 带参数的init
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度为{self.width}，高度为{self.height}。')

    def __str__(self):
        return '洗衣机'  # 只能return字符串类型数据

    def __del__(self):
        print(f'对象{self}已被删除')  # 默认self是对象内存地址，定义了__str__()则self为return中的数据

Haier1 = Washer()  # 实例化
print(Haier1)  # 默认打印内存地址，定义了__str__()方法则打印该方法中return的数据
Haier1.wash()  # 调用实例方法，self调用了Haier对象

# 添加、获取、删除对象属性
'''
①类外面添加对象属性
  对象名.属性名 = 值
②类外面获取对象属性
  对象名.属性名
③类里面获取对象属性
  self.属性名
④删除对象属性
  del 对象名.属性
'''
Haier1.width = 500
print(f'Haier1洗衣机的宽度是{Haier1.width}。')
print(Haier1.__dict__)  # __dict__以字典形式查询对象属性
# 魔法方法
'''
①__xx__()形式的函数称为魔法方法，是具有特殊功能的函数，满足特定条件会自动调用
②__init__()  初始化对象，在创建对象时默认调用，无需手动调用
 带参数：__init__(x, y, z)
③__str__()
  1.只能返回str类型数据
  2.将对象转为str类型时会执行该方法。print打印对象时会执行该方法，因为进行了隐式数据类型转换，即str(对象)

④__del__()
  1.删除对象时自动调用该方法，程序结束后对象将统一自动执行该方法
  2.如果同一个内存空间被多个变量引用，只有在所有引用都被del才会被删除，除非程序结束
'''
Haier2 = Washer()
Haier2.print_info()

Haier3 = Washer()
Haier3.__int__(300, 300)  # 带参数的init方法
# 因为init方法创建时就会被调用，上两句可简写为Haier3 = Washer(300, 300),即实参写入类括号中
Haier3.print_info()
print(Haier3.__str__())  # str
del Haier3  # del
