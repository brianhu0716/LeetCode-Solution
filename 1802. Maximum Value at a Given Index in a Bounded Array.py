# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 08:54:01 2021

@author: Brian
"""

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        target = max(2,maxSum // n) # 強迫除target外每一個數字至少是1，target至少為2
        #print(target)
        c = 0
        for i in range(index,-1,-1):
            maxSum -= (num := max(target - c,1))
            if num == 1 and 'lp' not in locals():
                lp = i
            c += 1 
        (lp := 0) if 'lp' not in locals() else lp
        
        c = 1
        for i in range(index + 1,n,1):
            maxSum -= (num := max(target - c,1))
            if num == 1 and 'rp' not in locals():
                rp = i
            c += 1 
        (rp := n - 1) if 'rp' not in locals() else rp

        
        #print(maxSum,lp,rp)
        
        if maxSum < 0 :
            return target - 1
        while maxSum >= 0:
            maxSum -= (rp - lp + 1)
            if lp == 0 and rp == n - 1:
                return maxSum // n
            elif lp == 0 or rp == n - 1:
                (lp := lp - 1) if (rp == n - 1) else (rp := rp + 1)
            else:
                lp -= 1
                rp += 1
        
            if maxSum == 0:
                return target + 1
            elif maxSum < 0:
                return target
            else:
                target += 1
            #print(maxSum,lp,rp)
                
test = Solution()
n = [4,4,3,4]
index = [0,2,0,0]
maxSum = [4,6,815094800,6]
for i in range(len(n)):
    if i == 2:
        print(test.maxValue(n[i], index[i], maxSum[i]))
        
    '''
1
2
271698267
2'''