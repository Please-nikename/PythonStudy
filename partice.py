# 问答程序

# 引入Question的资料模组

from question_for_partice import Question  
# 这里的意思是从question_for_partice算法文件中仅仅引入Question这个自建模组(档案)，不会引入别的东西，如果有别的东西的话

#第一步：先在列表中把所有的问题全部列出 
test = [
    '1+3 = ?\n(a) 2\n(b) 3\n(c) 4',
    '1 mter equal to how many centermeter? /n(a) 10 /n(b) 100 /n(c)1000',
    'What colour is the banana? /n(a) yellow /n(b) red /n(c) green'
]

#第二步： 在另外一个算法文件中创建一个单独的 Question class 定义它的两个属性，问题描述和答案

#第三步： 使用from question_for_partice import Question  调用单独创建的文件夹中的class

#第四步： 创建列表，将class中每个问题和它的答案存为呼叫列表
questions = [
    Question(test[0],'c'),
    Question(test[1],'b'),
    Question(test[2],'a')
]

# 第五步： 定义一个跑测验的函数
def run_test(questions):
    score = 0  # 启示分数为0
    for question in questions: #使用for做列表循环
        solution = input(question.description) # input(question.description)表示受测者需要输入答案，并将受测者的答案赋给solution
        if solution == question.solution: # 判断答案是否正确
            score += 1 # 正确则加一

    print('you get '+ str(score)+' for '+str(len(questions))+' questions')

run_test(questions)











