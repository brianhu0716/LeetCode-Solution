# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:34:12 2021

@author: -
"""
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["4","-2","/","2","-3","-","-"]
tokens = [int(v) if (v != "+" and v != "-" and v != "*" and v != "/") else v for i,v in enumerate(tokens)]
i = 0
while True:
    if tokens[i] == '+':
        tokens[i - 2] = tokens[i - 2] + tokens[i - 1]
        del tokens[i - 1:i + 1] # 移除位置i-1以及i的值
        i = i - 1 # 由i - 1開始下一輪搜索
    elif tokens[i] == '-' :
        tokens[i - 2] = tokens[i - 2] - tokens[i - 1]
        del tokens[i - 1:i + 1]
        i = i - 1
    elif tokens[i] == '*' : 
        tokens[i - 2] = tokens[i - 2] * tokens[i - 1]
        del tokens[i - 1:i + 1]
        i = i - 1
    elif tokens[i] == '/' :
        tokens[i - 2] = int(tokens[i - 2] / tokens[i - 1])
        del tokens[i - 1:i + 1]
        i = i - 1
    else:
        i += 1
    
    if len(tokens) == 1:
        print(tokens[0])
        break