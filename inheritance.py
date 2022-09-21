#继承

from student_for_inheritance import Student

student1 = Student('andrea',27,'POLITO')
student1.print_age() # 在student中是没有print_age函数的，是从person里面继承过来的
student1.print_name()


