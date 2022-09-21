#String 如何使用字符串，字符串的用法
print('hello Mr.White')
print('hello \nMr.white') #使用\n作为换行符号
print('hello\"Mr.white') #使用\在文字中插入符号
print('hello'+'Mr.white')#使用+连接字符串

phrase = 'hello'
print(phrase+'Mr.white')

#字符串函数 String Function

phase = 'Hello Mr.White'

print(phase.lower()) #使用.lower()将所有的字符都变成小写
print(phase.upper()) #使用.upper()将所有的字符都变成大写 

print(phase.isupper()) #使用.isupper()判断字符串是否都为大写
print(phase.islower()) #使用.islower()判断字符串是否都为小写

print(phase.lower().islower()) #可以连续叠加使用函数,但是仅返回最后一个函数值

phase = 'Hello Mr.White'
        #0123456789...
print(phase[1]) #中括号里的数值表示返回字符串中的'1'第一个字母,但是注意会返回'e'是应为在PYTHON中所有的计数都是从0开始算
print(phase[6])

print(phase[0:5]) # 提取字符串Hello，根据字符串中字符的位置
print(phase[6:])  # 提取字符串Mr.White

print(phase.index('H')) # 寻找字符串中字符'H'的位置，返回位置信息
print(phase.index('l')) # 如果想要寻找的字符有很多个，则这个函数中仅返回第一个字符的位置

print(phase.replace('H','h')) #使用.replace('','')用于替换原字符串中的某个字符，第一个引号中为被替换的字符，第二个引号中为替换成的字符
print(phase.replace('l','L')) #.replace会替换字符串中所有相同字符

print(phase.replace('l','L').replace('M','m')) # replace 也可以叠加





