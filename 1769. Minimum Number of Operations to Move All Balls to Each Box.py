# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:02:03 2021

@author: Brian
"""
boxes = "001011"
# boxes = "110"
boxes = [int(i) for i in boxes]
count,ans = 0,[]
while count < 2:
    (boxes := boxes) if count % 2 == 0 else (boxes := boxes[::-1]) 
    accu_ball = [0]
    accu_step = [0]
    for i in range(1,lb := len(boxes)):
        if boxes[i - 1] == 0:
            accu_ball.append(accu_ball[-1])
            accu_step.append(accu_ball[-1] + accu_step[-1])
        else:
            accu_ball.append(accu_ball[-1] + 1)
            accu_step.append(accu_ball[-1] + accu_step[-1])
    (accu_step := accu_step) if count % 2 == 0 else (accu_step := accu_step[::-1])
    ans += [accu_step]
    count += 1
print([ans[0][i] + ans[1][i] for i in range(lb)])