#猜数字游戏

secret_num = 77
guess = None
guess_count = 0 
guess_limit = 3 #限制猜3次
out_of_limit = False # 是否超出了猜测次数限制

while secret_num != guess and not(out_of_limit) :
    guess_count += 1

    if guess_count <= guess_limit:
        guess = int(input('please enter the number')) 

        if guess > secret_num :
            print('Smaller')

        elif guess < secret_num :
            print('Bigger')

    else:
        out_of_limit = True # 当 out_of_limit = True，也就是当guess_count 不再小于 guess_limit，则跳出while循环
        
if out_of_limit:
    print('U lost')
else:
    print('Binggo')














