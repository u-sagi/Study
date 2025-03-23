# 要求：将小于房子剩余面积的家具放入房子中
"""
分析：
①两个类，房子和家具
②房子属性：地理位置，总占地面积，剩余空间面积，房子内家具列表。
  方法：容纳家具。  显示；房子所有信息
 家具属性：家具名称，家具占地面积
"""


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House:
    def __init__(self, pos, area):  # 房子初始属性
        self.pos = pos
        self.area = area
        self.free_area = area
        self.furnitureList = []

    def move(self, furniture):  # 搬家具方法
        if furniture.area <= self.free_area:
            self.furnitureList.append(furniture.name)
            self.free_area -= furniture.area
        else:
            print(f'房子剩余占地面积不足，家具<{furniture.name}>无法搬入房中。')

    def __str__(self):  # 展示房子总体信息
        return f'房子位于{self.pos}，拥有占地面积{self.area}，目前剩余面积{self.free_area}，' \
               f'内有家具{self.furnitureList}。'

# 实例化
sofa = Furniture('沙发', 10)  # 直接将实参写进类括号中，不写将报错。
desk = Furniture('椅子', 2)
table = Furniture('桌子', 6)
bed = Furniture('床', 10)

home = House('北京', 20)
home.move(sofa)
home.move(desk)
home.move(table)
home.move(bed)
print(home)

