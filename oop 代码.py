"""
定义一个学生类，用来形容学生
"""
# 定义一个空的类
class Student1():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有，否则报错
    pass
# 定义一个对象
mingyue = Student1()

# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 定义变量
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'python'
    # 定义动作
    @property
    def doHomework(self):
        print('I 在做作业')

        # 推荐在函数末尾使用return语句
        return None
# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传入进参数
yueyue.doHomework


class Student():
    name = "dana"
    age = 18
yueyue = Student
print(Student.__dict__)
print(yueyue.name)

class A():
    name = "dana"
    age = 18
    # 注意say的写法，参数有一个self
    def say(self):
        self.name = 'aaaa'
        self.age = 200
# 此案例说明
# 类实例的属性和其对象实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量
# 此时,A成为类实例
print(A.name)
print(A.age)
print('*' * 20)
print(id(A.name))
print(id(A.age))
print('*' * 20)
a = A()
print(a.name)
print(a.age)
print('*' * 20)
print(id(a.name))
print(id(a.age))
print('*' * 40)
# 此时,A成为类实例
print(A.name)
print(A.age)
print('*' * 20)
print(id(A.name))
print(id(A.age))
print('*' * 20)
a = A()
# 查看A内所有属性
print(A.__dict__)
print(a.__dict__)
a.name = "yaona"
a.age = 16
print(a.__dict__)
print(a.name)
print(a.age)
print('*' * 20)
print(id(a.name))
print(id(a.age))
