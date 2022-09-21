# 进阶计算机
num1 = float(input("input fist number:"))
op = input("please enter the symble")
num2 = float(input('input sceond number: '))

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
else:                   # if the symble is not above
    print('DO NOT SUPPORT')

