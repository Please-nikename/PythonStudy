#类别class ，物件object
# 第一步创建资料形态class
class Phone : #  self,操作系统，型号，是否防水。后面三个参数是定义资料形态所需要的信息
    def __init__(self,os,number,is_waterproof): # '__init__'初始函数命名方式也就是某个物件初始的定义函数，self表示物件本身，信息定义物件
        self.os = os                            # self也就是物件本身有一个属性叫os，它的值等于我们输入的os的值
        self.number = number                    # self也就是物件本身有一个属性叫number，它的值等于我们输入的number的值
        self.is_waterproof = is_waterproof      # self也就是物件本身有一个属性叫is_waterproof，它的值等于我们输入的is_waterproof的值,同上
        
phone1 = Phone ('ios',123,True) # Object 1 :创建一个物件phone1 ,后面是它的属性

print(phone1.os) # 如果想要提取物件的某个属性信息，可以这样打印出来
print(phone1.number)

phone2 = Phone ('ios',678,False) # Object 2 
print(phone1.is_waterproof )






























