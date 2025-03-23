# 把八位老师随机分配到三个教室中
import random
classroom = [[], [], []]  # 三个教室
teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # 八位老师
for i in teacher:  # 遍历teacher
    rand = random.randint(0, 2)  # 随机取得任一教室的索引
    classroom[rand].append(i)  # 逐一把teacher中数据放入到上面索引对应的教室中
print(classroom)

