# 封装
'''
封装的用处：
1.方便迭代和维护
2.设置私有属性/方法，提高代码安全性
3.降低模块/类使用难度
'''

# 私有属性/方法
'''
1.私有方法
  __方法名称():
    pass
2.私有属性
  self.__属性名称 = 值

3.查询私有属性：对象.__dict__
4.外部调用私有属性：对象名._类名__私有属性名 
'''

class Person:
    def __drive(self):
        print("开始开车")

    def shopping(self):
        self.__drive()
        print("去购物了")

# 私有属性的修改、获取
'''
一般不会强行修改私有属性，而是定义方法用于修改
用处：可以在get/set方法中对进行原数据进行一些处理，如对输入的手机号脱敏处理
'''
class man:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

