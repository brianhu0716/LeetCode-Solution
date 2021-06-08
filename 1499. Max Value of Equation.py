# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:40:33 2021

@author: Brian
"""
points = [[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]]
k = 6
ans = float('-inf')
start = 1
for i in range((lp := len(points))):
    for j in range(i + 1,lp):
        if (diff := abs(points[i][0] - points[j][0])) <= k:
            ans = max(ans,diff + points[j][1] + points[i][1])
            print(i,j,ans)
        else:
            break
        
print(ans)

'''
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = float('-inf')
        
        r1,r2 = -inf,-inf
        if abs(points[0][0] - points[-1][0]) <= k and points[0][0] < 0 and points[-1][0] > 0:
            for i in range(lp := len(points)):
                if points[i][0] < 0 and points[i][1] > 0:
                    r1 = max(r1,points[i][1] - points[i][0])
                elif points[i][0] > 0:
                    break
            for j in range(i,lp):
                if points[j][0] > 0 and points[j][1] > 0:
                    r2 = max(r2,sum(points[j]))
            return r1 + r2
        
        start = 1
        for i in range((lp := len(points))):
            for j in range(i + 1,lp):
                if (diff := abs(points[i][0] - points[j][0])) <= k:
                    ans = max(ans,diff + points[j][1] + points[i][1])
                else:
                    break
        return ans