# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:52:16 2021

@author: Brian
"""
import numpy as np
class Solution:
    def checkIfExist(self, arr):
        self.pairs = list()
        self.arr_sort = np.sort(arr)
        Nind = np.where(self.arr_sort < 0) # Nind is tuple, an index array in index [0]
        Nind = Nind[0] # Nind is an index array
        Nind = Nind[::-1] # reverse the order,方便設定搜索負值序列的條件 
        if Nind.size > 0:
            for negative in Nind:
                if self.arr_sort[Nind[-1]] / self.arr_sort[negative] < 2:
                    break
                else:
                    if 2*self.arr_sort[negative] in self.arr_sort[Nind]:
                        self.pairs += [(self.arr_sort[negative],2*self.arr_sort[negative])]    
        Pind = np.where(self.arr_sort > 0)
        Pind = Pind[0]
        if Pind.size > 0:
            for positive in Pind:
                if self.arr_sort[Pind[-1]] / self.arr_sort[positive] < 2:
                    break
                else:
                    if 2*self.arr_sort[positive] in self.arr_sort[Pind]:
                        self.pairs += [(self.arr_sort[positive],2*self.arr_sort[positive])] 
        Zind = np.where(self.arr_sort == 0)
        if Zind[0].size >= 2 or all(self.arr_sort == 0):
            self.pairs += [(0,0)]
        return bool(self.pairs)
'''
questions = np.array([[10,2,5,3],
                        [7,1,14,11],
                        [3,1,7,11]]) 
                        '''
''' 多維陣列要用[[~],
                [~],    
                [~]]'''
'''
for i in range(questions.shape[0]):
    test = Solution()
    test.checkIfExist(arr = questions[i])
'''        
test = Solution()
questions = np.array([-10,12,-20,-8,15])
test.checkIfExist(questions)
bool(test.pairs)
            
            
            