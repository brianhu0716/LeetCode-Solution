# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:08:38 2021

@author: Brian
"""
# import collections
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3

cars = [[1,2],[2,1],[4,3],[7,2]]
ans = [-1] * len(cars)
acc_t = 0
while True:
    print(cars,"長度",len(cars))
    rest = []
    for i in range(len(cars) - 1):
        if cars[i][1] > cars[i + 1][1]:
            rest.append((cars[i + 1][0] - cars[i][0]) / (cars[i][1] - cars[i + 1][1]))

    if not rest:
        break
    else:
        acc_t += min(rest)
        merge_index = []
        cars[0][0] += min(rest) * cars[0][1]
        for i in range(1,len(cars)):
            cars[i][0] += min(rest) * cars[i][1]
            if cars[i][0] == cars[i - 1][0]:
                cars[i - 1][1] = min(cars[i - 1][1],cars[i][1])
                merge_index.append(i)
                ans[i - 1] = acc_t
    
        for i in merge_index[::-1]:
            cars.pop(i)
    

print(ans)