# 物件函数

class Phone : #  self,操作系统，型号，是否防水。后面三个参数是定义资料形态所需要的信息
    def __init__(self,os,number,is_waterproof,istouchable): # '__init__'初始函数命名方式也就是某个物件初始的定义函数，self表示物件本身，信息定义物件
        self.os = os                            # self也就是物件本身有一个属性叫os，它的值等于我们输入的os的值
        self.number = number                    # self也就是物件本身有一个属性叫number，它的值等于我们输入的number的值
        self.is_waterproof = is_waterproof 
        self.istouchable = istouchable

   # 在类别class中可以宣告别的函数来使用
   
    def is_ios(self):  # 创建函数判断系统是否为IOS
        if self.os == 'ios':
            return True
        else:
            return False

    def touchable(self):
        if self.istouchable == 'touchable':
            return True
        else:
            return False

    def add(self,num1,num2): # 增加一个加法器的属性
        return num1+num2



phone1 = Phone('ios','123','is_waterproof','not_touchable')
print(phone1.is_ios())   # 布尔判断
print(phone1.touchable()) # 布尔判断
print(phone1.add(7,8))