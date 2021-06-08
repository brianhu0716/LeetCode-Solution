# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:29:51 2021

@author: Brian
"""

class Solution:
    def findNextIncreaseSeq(self,start,end,ratings):
        self.equal = False
        for i in range(start,end - 1):
            if ratings[i + 1] >= ratings[i]:
                if ratings[i + 1] == ratings[i] : self.equal = True
                    
                return i
            
        return end - 1

    def candy(self, ratings: List[int]) -> int:
        N_candy = list()
        i,lr = 0,len(ratings)
        
        if lr == 1: return 1
        
        while i < lr - 1:
            if ratings[i] < ratings[i + 1]:
                if i == 0 : N_candy.append(1)
                    
                N_candy.append(N_candy[-1] + 1)
                
                i += 1
            else: # ratings[i] >= ratings[i + 1]:
                new_start = self.findNextIncreaseSeq(i,lr,ratings) 
                
                update_val = new_start - i + 1
                
                if not N_candy or update_val >= N_candy[-1]:
                    if N_candy : N_candy.pop()
                        
                    N_candy += [i for i in range(update_val,0,-1)]
                    
                else:
                    N_candy += [i for i in range(update_val - 1,0,-1)]
                    
                if self.equal : 
                    N_candy.append(1)
                    new_start += 1
                    
                i = new_start
                
        return sum(N_candy)