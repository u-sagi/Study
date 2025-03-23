def systemInfo():
    print('-' * 40)
    print('欢迎使用学员管理系统')
    print('1.增加学员信息')
    print('2.删除学员信息')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.显示所有学员信息')
    print('0.退出系统')
    print('-' * 40)

def addStudentInfo(name, age, gender):  # 添加
    temp = {'name': name, 'age': age, 'gender': gender}
    global student
    student.append(temp)
    print("添加成功！")
    return 1

def deleteStudentInfo(name):  # 删除
    i = queryStudentInfo(name)
    if i != -1:
        del student[i]
        print("删除成功！")
        return 1
    print("删除失败，无此姓名的学员，请重新尝试。")
    return -1

def changeStudentInfo(name):  # 修改
    global student
    i = queryStudentInfo(name)
    if i != -1:
        student[i]['age'] = int(input(f'将{name}的年龄修改为：'))
        student[i]['gender'] = input(f'将{name}的性别修改为：')
        print("修改成功！")
        return 1
    else:
        print("修改失败，无此姓名的学员，请重新尝试。")
        return -1


def queryStudentInfo(name):  # 查询
    """
    :param name: 学员姓名
    :return: 返回对应的下标，否则返回-1
    """
    global student
    for i in student:
        if i['name'] == name:
            return student.index(i)
    return -1

def showStudentInfo():  # 显示所有
    global student
    if len(student) != 0:
        print(f'+-------+-------+-------+')
        print(f'|  姓名\t|  年龄\t|  性别\t|')
        for i in student:
            print(f"|  {i['name']}\t|  {i['age']}\t|  {i['gender']}\t|")
            print(f'+-------+-------+-------+')
    else:
        print("当前学员数据为空。")

student = []
user_num = -1
while user_num != 0:
    systemInfo()
    user_num = int(input("请输入功能序号："))
    if user_num == 1:  # 增加学员信息
        name = input("请输入学员姓名：")
        if queryStudentInfo(name) == -1:
            age = int(input("请输入学员年龄："))
            gender = input("请输入学员性别：")
            addStudentInfo(name, age, gender)
        else:
            print("该学员信息已存在。")
    elif user_num == 2:  # 删除
        name = input("请输入要删除学员姓名：")
        deleteStudentInfo(name)
    elif user_num == 3:  # 修改
        name = input("请输入要修改信息的学员姓名：")
        changeStudentInfo(name)
    elif user_num == 4:  # 查询
        name = input("请输入要查询信息的学员姓名：")
        i = queryStudentInfo(name)
        if i != -1:
            print(f"姓名：{student[i]['name']}, 年龄：{student[i]['age']}, 性别：{student[i]['gender']}")
        else:
            print("查无此姓名的学员，请重新尝试。")
    elif user_num == 5:  # 显示所有
        showStudentInfo()
    elif user_num == 0:  # 退出
        print("退出成功。")
        break
    else:
        print("输入有误，请重新输入。")


