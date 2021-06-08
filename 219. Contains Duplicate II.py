# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:12:07 2021

@author: Brian
"""
'''
在k的範圍內搜尋子字串是否有重複出現的字，本題解題時以字典輔助，演算流程如下
(a) 如果k值大於資料總長度，則直接遍歷字串做'一次判斷'，若有'鍵'對應的'值'等於2，則回傳true，否則false
(b) 若值小於資料總長度：
    (b.1) 先取前k個子字串做第一次判斷並建立字典，若有'鍵'對應的'值'等於2，則回傳true，否則初始值將起始值(i)+1
          且將原子字串的第一個值對應到的鍵的值-1，進(b.2)
    (b.2) 此時我們只要對位移一個位置的子字串的最後一個數字對應到的鍵做判斷，若已經有該鍵存在，則直接回傳True
          否則進入(b.3)
    (b.3) 重複(b.2)直到所有範圍內的子字串都遍歷後結束
'''
class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        ln = len(nums)
        i = 0
        self.dict1 = {}
        if k >= ln:
            self.judgeRepeat(nums[i:])
            return self.frep
        else:
            while i < ln - k:
                sample = nums[i:i + k + 1]
                if i == 0:
                    self.judgeRepeat(sample)
                    if self.frep:
                        return True
                    else:
                        self.dict1[sample[0]] -= 1
                        i += 1           
                else:
                    self.judgeRepeat([sample[-1]])
                    if self.frep:
                        return True
                    else:
                        self.dict1[sample[0]] -= 1
                        i += 1
            return False
        
    def judgeRepeat(self,x):
        self.frep = False
        for i in range(len(x)):
            if x[i] not in self.dict1.keys():
                self.dict1[x[i]] = 1
            else:
                self.dict1[x[i]] += 1
                if self.dict1[x[i]] == 2:
                    self.frep = True
                    break  
                else:
                    continue
        '''
        print(list(self.dict1.keys()))
        print(list(self.dict1.values()))
        print('\n')
        '''