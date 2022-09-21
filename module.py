# Use of module

import tool_example_for_module # 自建模组（函数库），也可以调用官方内建模组

print(tool_example_for_module.name) #调用tool中的单一信息

print(tool_example_for_module.mux_num(15,16,58)) # 调用tool中的函数，直接呼叫函数

# 如果想查某个官方模组的内容
import token # 调某个用官方模组
import sys #  打开系统模组
print(sys.path) # 打印出token模组的系统路径  'D:\\python3.10\\lib' 这种以lib 结尾的就是python内建模组的存放地，可以用(ctrl+click)打开文件


# 也可以下载第三方的模组
# pip 套件管理工具
# 范例：pip install pygame
# 如果想给模组改名 ： import pygame as pg 改名为pg
import pygame









