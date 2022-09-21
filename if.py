# if 判断句

#Ex1
#if i am hungary
#     i go to eat
hungary = True
if hungary:
    print('i go to eat')


#Ex2
#if today is rain
#     I take my car
#else
#     i go with walk
rain = False  # 布尔值的判断，Boolean judgment
if rain:
    print('I take my car')
else:
    print('i go with walk')


#Ex3
#if you get 100
#     i give you 1000$
#else if you get over 80
#     i give you 500$
#else if if you get over 60
#     i give you 100$
#else
#     you give me 2000$
rank =30
if rank == 100:
    print('i give you 1000$')
elif rank>=80:
    print('i give you 500$')
elif rank>=60:
    print('i give you 100$')
else:
    print('you give me 2000$')

#Ex4
#IF YOU GET 100RANK AND TODAY IS RAIN
#   THEN I GIVE YOU 100$
#ELSE IF 
#   YOU GIVE ME 100$
score = 100
rain = True
if score == 100 and rain:
    print('i give you 100$')
else:
    print('you give me 100$')

#Ex5
#IF YOU GET 100RANK OR TODAY IS RAIN
#   THEN I GIVE YOU 100$
#ELSE IF 
#   YOU GIVE ME 100$
score = 50
rain =False
if score == 100 or rain:
    print('i give you 100$')
else:
    print('you give me 100$')


#Ex6
#IF YOU GET 100RANK OR TODAY IS  NOT RAIN
#   THEN I GIVE YOU 100$
#ELSE IF 
#   YOU GIVE ME 100$
score = 50
rain = True
if score == 100 or not(rain):
    print('i give you 100$')
else:
    print('you give me 100$')



#Ex7
#IF YOU NOT GET 100RANK OR TODAY IS  NOT RAIN
#   THEN I GIVE YOU 100$
#ELSE IF 
#   YOU GIVE ME 100$
score = 50
rain = True
if score != 100 or not(rain):# score != 100 '!='的意思是判断左边和右边是否不等
    print('i give you 100$')
else:
    print('you give me 100$')

# EXERCIXE: MAX_NUMBER
def mux_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else :
        return num3

print(mux_num(10,20,30))
 

