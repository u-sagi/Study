# 类属性
'''
1.类属性所有对象共有
2.获取类属性：类名.属性  （如果对象中无同名属性，则也可以通过对象点出）
3.修改类属性：类名.属性 = 值
  如果使用 对象.属性 = 值 则会添加实例属性
'''

# 类方法
'''
@classmethod
def 类方法名(cls):
    pass
1.当方法中用不到实例属性，但用到了类属性/类方法，则使用类方法
'''


class Apple(object):
    num = 10

    def __init__(self):
        self.eat_num = 0

    def eat(self):
        self.eat_num += 1
        Apple.num -= 1

    @classmethod
    def eat_apple_num(cls):  # cls代表当前类的类名
        print(f'被吃掉了{10-cls.num}个苹果，还剩{cls.num}个。')

a1 = Apple()
a2 = Apple()
a3 = Apple()
a1.eat()
a1.eat()
a2.eat()
a3.eat()
Apple.eat_apple_num()

# 静态方法
'''
既用不到实例属性/方法，也用不到类属性/方法，则可以封装成静态方法。
@staticmethod
def 方法名():
    pass
'''