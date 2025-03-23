# 列表 + 字典
# 字典可以存储一个人的基本信息,当要存储多个人的信息时，需结合列表
"""
students = [{'name': 'Ella', 'age': 20},\
            {'name': 'Tom', 'age': 19},\
            {'name': 'Ham', 'age': 20}]
"""
students = []
print('-' * 40)
print('欢迎使用通讯录管理系统')
print('1.增加学员信息')
print('2.删除学员信息')
print('0.退出系统')
print('-' * 40)
user_num = -1
while user_num != 0:
    user_num = int(input('请输入你要进行的操作对应的数字：'))
    if user_num == 1:
        student = {}  # 每次循环到这都重新定义空字典student
        student['name'] = input('请输入学生姓名：')
        student['age'] = int(input('请输入学生年龄：'))
        student['gender'] = input('请输入学生性别：')
        students.append(student)
        print(students)
    elif user_num == 2:
        s_name = input('请输入要删除的学生的姓名：')
        for i in students:
            if i['name'] == s_name:
                students.remove(i)
                print('删除成功！')
                print(students)
            else:
                print('输入有误或姓名不存在。')
    elif user_num == 0:
        print('退出成功。')
        break
    else:
        print('输入有误，请重新输入。')
