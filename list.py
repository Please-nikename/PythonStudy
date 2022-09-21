#列表，列表的用法（集合）
scores = [90,70,60,60,50] #数值列表

students = ['A','B','C','D','E'] #字符串列表

things = [90,'A',True] #数字+字符+布尔值 列表

scores[0] = 30 #替换，将列表中第0位的数字改成30

#列表中常用的函数
scores.extend(students) # .extend 列表拓展，把students中的内容接到scores后面
scores.append(45) # .append添加 列表拓展，增加特定数值或者字符
scores.insert(2,30) # .insert插入，在列表的第二位，插入特定数值30
scores.clear() # .clear清除整个列表
scores.pop() # .pop清除列表最后一位的内容
scores.sort()# .sort对列表里的数据从小到大进行排序
scores.reverse() # .reverse表示将列表里的内容反转，首尾互换

print(scores)

print(scores.index(60)) # 返回所选值在列表中的位置，仅返回第一个找到的相同值
print(scores.count(60)) # 返回列表中数字60的个数

print(scores[0]) #提取特定位置的内容，从0位开始计算，正向计数
print(scores[3])

print(scores[-1]) # 提取倒数第一位
print(scores[-3]) # 提取倒数第三位
print(scores[0:2]) # 提取列表中的前两位内容，从0位开始取，到第二位但是不包括第二位，90，70
print(scores[1:4]) # 提取从第1位开始往后，到第4位，但是不包含第四位70，60，65
print(scores[1:]) # 提取从第一位开始后面所有位的内容
print(scores[:4]) # 从头开始提取到第四位，但是不包含第四位













