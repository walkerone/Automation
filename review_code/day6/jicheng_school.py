# Author:zhang
# -*- coding:utf-8 -*-
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []
        self.course = []
        self.gradge = []

    def hire(self, staff_obj):
        print("雇佣新员工 %s" % staff_obj.name)
        print("XXXXXXXXXXXXXX")
        self.staffs.append(staff_obj)

    def enroll(self, stu_obj):
        print("为 %s 办理注册额手续" % stu_obj.name)
        self.students.append(stu_obj)

    def create_course(self, course_type, price, time):
        self.course.append(Course(course_type, price, time))

    def creart_gradge(self, gradge_level):
        self.gradge.append(Gradge(gradge_level))


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teache(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teache, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        --- info_testint---
        name,%s
        age,%s
        sex,%s
        salary,%s
        course,%s
        ''' % (self.name, self.age, self.sex, self.salary, self.course)
              )

    def teach(self):
        print("%s is teaching course [%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, gradge_obj):
        super(Student, self).__init__(name, age, sex)
        self.gradeg_obj = gradge_obj

    def tell(self, school_obj):
        print('''
        ---info---
        name,%s
        age,%s
        sex,%s

        ''' % (school_obj.name, self.gradeg_obj.name, self.name, self.age, self.sex,)
              )

    def pay_tuiton(self, amount):
        print("%s has paid tution for %s" % (self.name, amount))


class Course(School):
    def __init__(self, type, price, time):
        self.type = type
        self.price = price
        self.time = time


class Gradge(object):
    def __init__(self, gradge_level, couser_type):
        self.gradge_level = gradge_level
        self.couser_type = couser_type

    def student_entroll(self,student_obj):
        print()


school = School("老男孩", "沙河")
t1 = Teache("老男孩", "55", "MF", "20000", "linux")
t2 = Teache("Alex", "22", "M", "300", "PythonDelovps")

s1 = Student("陈荣华", "36", "MF", "1001", "Pythondevlops")
s2 = Student("xulianwei", "22", "M", "1002", "Pythondevlops")
t1.tell()
s1.tell()
school.enroll(s1)
school.hire(t1)
print(school.students)
print('---------8888')

print('999999999')
school.staffs[0].tell()
school.staffs[0].teach()
