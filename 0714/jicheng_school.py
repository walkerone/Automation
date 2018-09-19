# Author:zhang
# -*- coding:utf-8 -*-
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staff = []

    def enroll(self, stuobj):
        print('为学员 %s 办理注册手续 ' % stuobj.name)
        self.students.append(stuobj)

    def hire(self, staff_obj):
        self.staff.append(staff_obj)

        print('为学员 %s 办理注册手续 ' % staff_obj.name)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---info--Teacher
        name:%s
        age:%s
        sex:%s
        salary:%s
        course:%s
        ''' % (self.name, self.age, self.sex, self.salary, self.course))

    def teache(self):
        print("%s is teachig course [%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ---info--Student---
        name:%s
        age:%s
        sex:%s
        stu_id:%s
        grade:%s
        ''' % (self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has pais tution %s " % (self.name, amount))
        print("哈哈")


school = School('老男孩IT', '沙河')
t1 = Teacher('oldboy', 56, 'MF', 20000, 'Linux')
t2 = Teacher('Alex', 23, 'M', 3000, 'Python')

s1 = Student('chenronghua', 36, 'mf', 1001, 'Pythondevlops')
s2 = Student('徐梁伟', 18, 'm', 1002, 'Linux')
t1.tell()
s2.tell()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)
print(school.students)
print(school.staff)
school.staff[0].teache()

for stu in school.students:
    stu.pay_tuition(500)
