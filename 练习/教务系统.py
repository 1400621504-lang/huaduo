from random import choice


class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名{self.name} | 语文{self.chinese} |数学{self.math} |英语{self.english} |总分{self.chinese+self.math+self.english}"

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self,chinese = chinese
        if math is not None:
            self,math = math
        if english is not None:
            self,english = english


class Edumanagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []


    def add_student(self):
        name = input("请输入学生的姓名")
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在，添加失败")
                return
        chinese  = int(input("请输入学生语文成绩"))
        math = int(input("请输入学生数学成绩"))
        english = int(input("请输入学生英语成绩"))

        if 0<chinese<=100 and 0<math<=100 and 0<english<=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功 ～")
        else:
            print("分数在0 - 100 之间！")

    def update_student(self):
       name = input("请输入需要修改的学生名")

       for s in self.student_list:
           if s.name == name:
               print(f"当前成绩是：{s}")

               chinese = input("请输入修改后学生语文成绩")
               math = input("请输入修改后学生数学成绩")
               english = input("请输入修改后学生英语成绩")

               if 0 < chinese < -100 and 0 < math <= 100 and 0 < english <= 100:
                   s.update_core(chinese,math,english)
                   print("当前成绩修改成功！")
                   print(f"修改后的成绩{s}")
                   return
               else:
                   print("分数得在0 - 100之间！")
                   return
       print("未找到该学生，寻找失败！")


    def delet_studengt(self):
       name = input("请输入删除的学生名字")

       for s in self.student_list:
           if s.name == name:
               self.student_list.remove(s)
               print("学生删除成功！")
               return
       print("未找到该学生，删除失败")
       return

    def show_student(self):
       name = input("输入你要查询的学生的名字")
       for s in self.student_list:
           if s.name == name:
               print(f"学生信息{s}")
               return
       print("未找到该学生！")

    def list_student(self):
       for s in self.student_list:
           print(s)


    def run(self):
       print(f"欢迎使用教务管理系统 V:{Edumanagement.system_version}")

       while True:
           print()
           print("#   #" * 20)
           print("###1.查询学生 2.修改学生 3.删除学生 4.查询学生 5.查询所有学生 6退出系统###" )
           print("#   #" * 20)
           choice  = input("\n请输入你要执行的操作 ：1-6  :")
           match choice:
               case "1":
                   self.add_student()
               case "2":
                   self.update_student()
               case "3":
                   self.delet_studengt()
               case "4":
                   self.show_student()
               case "5":
                   self.list_student()
               case "6":
                   print("bye")
                   break


if __name__ == "__main__":
    # s1 = Student("张三",100,22,33)
    # print(s1)
    edu = Edumanagement()
    edu.run()
