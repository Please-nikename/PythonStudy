# 会发现在person中和Student中有很多的信息属性相同，这时可以使用继承的手法来减少工作量
# 属性多的类别继承属性少的类别，这里就是student继承person
# 相当于Person中的资料复制一份到了Student的最上面

from Person_for_inheritance import Person

class Student(Person):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    
    def print_school(self):
        print(self.school)