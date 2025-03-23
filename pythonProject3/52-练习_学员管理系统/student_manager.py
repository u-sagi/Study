"""
需求：
1.根据输入数字执行不同命令
2.增/删/改/查学员，查询所有学员，退出程序，展示开始界面
"""
from student import Student


class StudentManager(object):
    def __init__(self):
        self.students = []

    @classmethod
    def showInfo(cls):
        print('选择如下功能————————')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.查看所有学员信息')
        print('6.保存学员信息')
        print('0.退出')

    def chooseOption(self, inputNum):
        if inputNum == '0':
            self.exitSystem()
        elif inputNum == '1':
            self.addStudent()
        elif inputNum == '2':
            self.removeStudent()
        elif inputNum == '3':
            self.changeStudent()
        elif inputNum == '4':
            self.queryStudent()
        elif inputNum == '5':
            self.queryAllStudent()
        elif inputNum == '6':
            self.saveStudentInfo()
        else:
            print('输入有误，请重新输入。')

    def exitSystem(self):
        print('退出成功。')
        self.loadStudentInfo()
        exit()


    def addStudent(self):
        studentId = input('请输入学员id：')
        if self.__getStudentIndex(studentId) != -1:
            print('你输入的学员id已存在，请重新输入。')
            return
        name = input('请输入学员姓名：')
        age = int(input('请输入学员年龄：'))
        self.students.append(Student(studentId, name, age))
        print('添加学员成功。')

    def removeStudent(self):
        id = input('请输入要删除学员的id：')
        index = self.__getStudentIndex(id)
        if index == -1:
            print('该学员不存在，请重新输入。')
        else:
            self.students.pop(index)
            print(f'{id}删除成功。')

    def changeStudent(self):
        id = input('请输入要修改学员的id：')
        index = self.__getStudentIndex(id)
        if index == -1:
            print('该学员不存在，请重新输入。')
        else:
            new_name = input(f'当前学员姓名为：{self.students[index].name},修改为：')
            new_age = input(f'当前学员年龄为：{self.students[index].age},修改为：')
            self.students[index].name = new_name
            self.students[index].age = new_age
            print(f'修改成功。修改后的学员信息：\n{self.students[index]}')

    def queryStudent(self):
        i = input('请输入学员id: ')
        for student in self.students:
            if i == student.studentId:
                print(student)
                return
        print('该id不存在。')

    def queryAllStudent(self):
        if len(self.students) == 0:
            print('当前学员列表为空。')
        else:
            for student in self.students:
                print(student)

    # 存储学员信息
    def saveStudentInfo(self):
        if len(self.students) == 0:
            print('当前无任何学员信息，无需保存。')
            return
        f = open('studentinfo.txt', 'w')
        for student in self.students:
            for key, value in student.__dict__.items():
                f.write(str(key)+': ')
                f.write(str(value))
                f.write('\n')
            f.close()
        print('保存成功。')

    # 加载学员信息
    def loadStudentInfo(self):
        f = open('studentinfo.txt', 'r')
        content = f.readline()
        studentId = name = ''
        age = 0
        while content != '':
            if 'studentId' in content:
                studentId = content[content.find(': ') + 2:content.find('\n')]
            if 'name' in content:
                name = content[content.find(': ') + 2:content.find('\n')]
            if 'age' in content:
                age = int(content[content.find(': ') + 2:content.find('\n')])
            if studentId != '' and name != '' and age != 0:
                self.students.append(Student(studentId, name, age))
                studentId = name = ''
                age = 0
            content = f.readline()

    def __getStudentIndex(self, id: str) -> int:
        for student in self.students:
            if id == student.studentId:
                return self.students.index(student)
        return -1
