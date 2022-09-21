#如何使用数字，数字的用法

from cmath import sqrt
from math import ceil, e, floor #模组引入


print(8/(5.5+4))
print(8*5.5)
print(8//5.5) #整数除法，只取整数部分

num = -8.5659
print(num%5) #'%'除法取余数

#数字函数function
# str(num)由数字转为字符
print(str(num))
print('Print the nummber '+ str(num)) #数字转化为字符以后可以输出为字符串,注意，数字不转化为字符则不可以输出为字符串

# abs(num)取绝对值
print(abs(num))

# pow(num,num) 幂运算
print(pow(2,5))
print(pow(9,0))

# round(num) 对数值取四舍五入
print(round(num))

# floor(num) 对数字的小数点进行无条件舍去
print(floor(4.66))

# ceil(num) 对数字进行无条件进位5.32进位到6
print(ceil(5.32))

# sqrt(num) 对数字进行开根号
print(sqrt(num))

# max(num1,num2,num3,....) 返回数列中的最大值
num1 = e
num2 = 0.15461
num3 = 1.789551
print(max(num1,num2,num3))

# min(num1,num2,num3,....) 返回数列中的最小值
print(min(num1,num2,num3))


























