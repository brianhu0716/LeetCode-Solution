# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 19:44:39 2021

@author: Brian
"""
'''
*** 關鍵：任意最大值到之後的負數之間都不存在負數，因為負數必須被消除或是比之前的所有最大值都大的話
            會被堆疊在asteroids的前幾個位置
(a) 首先先找出序列中第一個出現的正整數，因為由左到右搜索時，如果面都是負數，不會有正數語之相抵，因此由
    一個出現的整數開始搜索，如果許列中沒有正數，回傳-1後直接結束搜索，若否則分幾種情況討論:
(b.1) 如果由第一個正數開始遇到正數的話，如果該值比之前的正數大，則更新該位置為最大值位置
(b.2) 如果遇到負數
    (b.2.1) 該負數若大於最大值，則直接將之前所有的正數全部移除，新的序列變為前面累積的幾個負數加上
            該負數位置之後的序列，組成新序列後找第一個正值，重複(b)，且新的起始點為該正數位置加1
    (b.2.1) 若該負數等於最大值，新序列為移除最大值到該負數之間的所有位置，組成新序列後找第一個正值
            重複(b)，且新的起始點為該正數位置加1
    (b.2.3) 若該負數小於最大值，新序列為移除該負數至大於或等於它的所有位置，組成新序列後不須找
            第一個正值，因為最大值依然有效，重複(b)，且新的起始點為抵銷的正數位置(加1為終點的
            正數大於該負數，不加1為終點的正數等於該負數)
(c) 重複(b)，直到索引值到達序列尾部，或所有的序列值已經為負
'''
class Solution:
    def findFirstPositive(self,asteroids):
        for i in range(0,len(asteroids)):
            if asteroids[i] > 0:
                return i
        return -1
    def findFirstNegative(self,asteroids,start):
        for i in range(start,-1,-1):
            if asteroids[i] < 0:
                return i
        return -1
    def asteroidCollision(self, asteroids):
        imax = self.findFirstPositive(asteroids)
        if imax == -1:
            return asteroids
        i = imax
        while i < len(asteroids):
            if asteroids[i] > 0 :
                if asteroids[i] >= asteroids[imax]:
                    imax = i
                i += 1
            else: 
                if abs(asteroids[i]) >= asteroids[imax]: # 該負數大於或等於之前的最大值
                    if abs(asteroids[i]) == asteroids[imax]: # 等於之前的最大值，將最大值與該負數之間的數字全部消除，重新第一個正值開始運算
                        asteroids = asteroids[:imax] + asteroids[i + 1:]
                    else: # 大於之前的最大值時，必須要先將最大值位置之前的所有負數都找到後，加上該負數之的所有值組成新的asteroids
                        asteroids = asteroids[:self.findFirstNegative(asteroids,i - 1) + 1] + asteroids[i:]
                    imax = self.findFirstPositive(asteroids) # 從len(l)開始找
                    if imax == -1:
                        return asteroids
                    else:
                        i = imax + 1
                else: # 該負數小於之前的的最大數
                    for j in range(i - 1,imax - 1,-1):
                        if abs(asteroids[i]) > asteroids[j]:
                            continue
                        else : # 找出該負數被終止的位置，此時因為最大值依然有效，故不需要再找從頭找最大值位置
                            if abs(asteroids[i]) < asteroids[j]:
                                asteroids = asteroids[:j + 1]  + asteroids[i + 1:]
                                i = j + 1
                            else :
                                asteroids = asteroids[:j] + asteroids[i + 1:]
                                i = j
                            break
        return asteroids
                
asteroids = [[1,-2,5,-9],
             [5,10,-5],
             [8,-8],
             [10,2,-5],
             [-2,-1,1,2]]

test = Solution()
for i in range(len(asteroids)):
    print(test.asteroidCollision(asteroids[i]))
        