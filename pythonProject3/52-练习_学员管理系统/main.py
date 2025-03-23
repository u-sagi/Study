# 主程序入口
# 一般开发中，文件夹使用大驼峰命名法，包/模块使用下划线分割法
from student_manager import StudentManager


def main():
    s1 = StudentManager()
    while True:
        # 提示用户输入信息
        StudentManager.showInfo()
        # 读取学员信息
        s1.loadStudentInfo()
        inputNum = input('请输入功能对应的数字：')
        s1.chooseOption(inputNum)

main()
