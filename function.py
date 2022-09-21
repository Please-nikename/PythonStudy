# 函数 Function


from multiprocessing.sharedctypes import Value

#ex1
def hello(name,age): # 定义函数 definition of the function
    print('Hello '+name+' your age is '+ str(age))

hello('Andrea',27) # 呼叫函数call for function,'27' must in string or use 'str()' to transfer the number to string

#ex2 加法器
def add(num1,num2):
    print(num1+num2)
    return 10  # return 10 后面的呼叫函数过程被数字10覆盖，函数内在return后面的操作不会在被执行,比如下面的 print('hello') 
    print('hello') # 不会被执行
print(add(2351866,7986230)) # 如果想返回信息，被覆盖的情况下就会返回数字10，如果不被return的值覆盖，则会返回输入的两个数字的和,print只显示计算结果

#ex3
def add(num1,num2):
    print(num1+num2)
    return num1+num2  # 这里用return中计算结果，是应为在print中可能可以做一些更多的计算过程，会用到此计算结果
print(add(2351866,7986230)*5) # 比如用第一次计算的结果*5

# ex4 
# Attention: it will return 4253 first and then return 10. 
# 第一步定义函数ADD，(27行)， 然后Value中呼叫了函数(31行)，然后返回运行函数(27行)，print相加的和(28行)
# 然后value被return的值10所覆盖(29,31行)，再次print数字10(32行)
def add(num1,num2):
    print(num1+num2)
    return 10  # return 10 后面的呼叫函数过程被数字10覆盖

Value=add(1535,2718)
print(Value) 

#ex5  过程同上，但是第二次print的信息为None
def add(num1,num2):
    print(num1+num2)
                      # 没有return的时候，则会自动认为:return None  

Value=add(1535,2718) 
print(Value)
