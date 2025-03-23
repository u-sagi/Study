# 子类中调用父类方法
"""
1.super().方法名()  调用当前类的上一级类的方法
2.类名.方法名(self)   直接调用对应类的方法，但该类必须在当前类的继承链中
3.super(要调用的父类的子类, self).方法名()
"""

# 多态
"""
1.多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，
  能产生不同执行结果
2.多态依赖继承
3.子类必须要重写父类方法
"""


def go_shopping(Driver):
    Driver.driver()


class Person(object):
    def driver(self):
        print("人开车")


class Man(Person):
    def driver(self):
        print("男人开车")


class Child(Man):
    def driver(self):
        print("小孩开车")


class Monkey(object):
    def driver(self):
        print("猴子骑单车")


go_shopping(Person())
go_shopping(Man())
go_shopping(Child())

go_shopping(Monkey())
# Monkey不在继承链中，但仍然能执行driver方法，语法没有问题，但逻辑
# 与多态完全不同，这种情况叫做“鸭子类型”（符合所有要求，但不是所要的）

# 子类中重写父类方法
"""
1.子类中重写父类方法无需关注参数是否一致，方法名相同则会被重写（）
"""
