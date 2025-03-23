"""
子类默认继承父类的【非私有】的所有属性和方法

单继承：一个类只能继承一个父类，大多数面向对象语言为单继承
多继承：一个类能继承多个父类，Python和C++支持多继承
    1.两个父类中如果有重名的方法/属性，则只会调用更靠前的父类的方法/属性
"""
# 拓展
"""
1. 父类如仅有一个初始化方法且带参，则子类实例化时也需传值
2. 查询继承类的链条：类名.__mro__
"""
# 父类A
class A(object):  # 所有类默认继承object类，又被称为顶级类或基类，其他子类称为派生类
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# 子类B
class B(A):  # 继承A的属性与方法
    pass

result = B()
result.info_print()
print(B.__mro__)
