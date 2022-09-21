# load and write

# open('档案路径',mode = '开启模式')
#绝对路径 ex: C:/Users/99714/Desktop/To be an Enginner/python stater/file load example.txt
#相对路径 以算法的位置做延伸，就是说得在同一个文件夹中 ex: file load example.txt

# mode = 'r'读取 load
# mode = 'w'覆写 overwrite
# mode = 'a'在原先的资料后添加东西  Continuation

# examples for ''r'
file = open('file load example.txt',mode = 'r',encoding='utf8')
print(file.read()) # 读取文件内容然后打印值
file.close() # 注意，打开文件以后一定要关上，不会占用电脑资源

file = open('file load example.txt',mode = 'r')
print(file.readline()) # 读取单一行文件内容，然后打印值77
print(file.readline())
file.close()

#file = open('file load example.txt',mode = 'r')
#for line in file: # 使用for循环，循环读取每一行的内容
#    print(line) # 打印，每一次循环读取的内容
#file.close()

#file = open('file load example.txt',mode = 'r')
#print(file.readlines()) # 读取文件内容,把每一行的资料都放入列表中
#file.close()


# examples for 'w'
file = open('file load example.txt',mode = 'w')
file.write('3\n4\n5\n6\n7\n8\n9\n')
file.close

# examples for 'a'
file = open('file load example.txt',mode = 'a',encoding='utf8')
file.write('MR.ANDREA')
file.write('\n周成璐') # 原本编码不支持中文的写入，打开文件的同时需要加上 encoding='utf8'
file.close

with open('file load example.txt',mode = 'a',encoding='utf8') as file: # 如果不想每次单独关闭文件，则可以使用with语句，将操作放在with语句中，就可以自动关闭
    file.write('\n你好')







