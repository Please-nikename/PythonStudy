# module模组使用的tool范例

name  = 'andrea' #单个信息
age = 27 # tool中的单个信息

def mux_num(num1,num2,num3):  # tool 中的函数
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else :
        return num3
