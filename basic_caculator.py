# 建立一个基本的计算机（相加）
name = input('please input your name :') #通过input给变量附值(字符串)
age = input('plaese input your age : ')
print(' Hello '+ name +', you are '+ age +' years old')



num1 = input('please input the first number')
num2 = input('please input the second number')
print(num1+num2) # 此处未将字符串转化为数字所以不会运行加法依然是字符串的连接

print(int(num1)+int(num2)) # int()可以将整数数字字符串转化为整数数字，但是int()只能用于整数，不然则无法识别
print(float(num1)+float(num2)) # float() 则可以转化非整数的数字



















