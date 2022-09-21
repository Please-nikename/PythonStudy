# for 循环 

# for 变量 in 字符串or列表：
#     要重复执行的算法

for letter in 'Hello Andrea': # 一次跑一个字符
    print(letter)

for num in [0,1,2,3,4,5]: # 跑几个循环取决于列表的长度
    print(num)

for num in range(100): # range相当于从0开始跑100次循环
    print(num)

for num in range(2,7): # range相当于从2到6,[2,3,4,5,6]，7不会算进去
    print(num)

# Ex. Power print(pow(2,5))
# 方法1 ：2*2*2*2*2
def power(base,power):
    result = base
    for index in range(power-1):
        result = result * base
    return result

print(power(2,5))

#方法2 ： 1*2*2*2*2*2
def power(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(power(2,5))








