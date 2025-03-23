# 学员类
class Student(object):
    def __init__(self, studentId: str, name: str, age: int):
        """传入id、姓名、年龄，初始化学员信息"""
        self.studentId = studentId
        self.name = name
        self.age = age

    def __str__(self):
        return f'学员id：{self.studentId}, 姓名：{self.name}, 年龄：{self.age}.'
