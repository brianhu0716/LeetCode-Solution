# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:14:57 2021

@author: Brian
"""
class Solution:
    def findRange2(self,insert,l,ln,i):
        r2 = []
        for j in range(i,ln):
            if j == ln - 1:
                self.start = ln - 1
                r2 if insert[1] > l[j][1] else (r2 := [l[j][0],insert[1]])
            elif insert[1] <= l[j][1] and insert[1] >= l[j][0]:
                r2 = [l[j][0],insert[1]]
                self.start = j
                break
            elif insert[1] > l[j][1] and insert[1] < l[j + 1][0]:
                self.start = j
                break
        if not r2:
            for k in range(i + 1,j + 1): # r2是空的,j也要算
                self.intersect += [l[k]]
        else:
            for k in range(i + 1,j):
                self.intersect += [l[k]]
            self.intersect += [r2]
            
    def findRange1(self,insert,l,ln):
        for i in range(self.start,ln):
            if insert[0] >= l[i][0] and insert[0] <= l[i][1]: # i等於ln - 1的情況只會出現在這裡
                if insert[1] >= l[i][1]:
                        self.intersect += [[insert[0],l[i][1]]]
                        self.findRange2(insert, l, ln, i)
                else:
                    self.intersect += [insert]
                    self.start = i
                    break
            elif insert[0] > l[i][1] and insert[0] < l[i + 1][0]:
                if insert[1] >= l[i + 1][0]:
                    self.findRange2(insert, l, ln, i)
                else:
                    self.start = i
                    break

        
    def intervalIntersection(self,firstList,secondList):
        self.start,self.intersect = 0,[]
        l1,l2 = len(firstList),len(secondList)
        if l1 >= l2:
            for insert in secondList:
                if insert[0] < firstList[0][0]:
                    if insert[1] < firstList[0][0]:
                        continue
                    else:
                        # self.intersect += [[firstList[0][0],insert[1]]]
                        self.findRange2(insert,firstList,l1,0)
                elif insert[0] > firstList[-1][-1]:
                    break
                else:
                    self.findRange1(insert,firstList,l1)
                
        else:
            for insert in firstList:                
                if insert[0] < secondList[0][0]:
                    if insert[1] < secondList[0][0]:
                        continue
                    else:
                        self.findRange2(insert,secondList,l2,0)
                        # self.intersect += [[secondList[0][0],insert[1]]]
                elif insert[0] > secondList[-1][-1]:
                    break
                else:
                    self.findRange1(insert,secondList,l2)
        

firstList = [[[0,2],[5,10],[13,23],[24,25]],
             [[1,3],[5,9]],
             [],
             [[1,7]],
             [[5,10]],
             [[14,16]],
             [[2,5],[7,8],[11,13],[18,20]]]
secondList = [[[1,5],[8,12],[15,24],[25,26]],
              [],
              [[4,8],[10,12]],
              [[3,10]],
              [[3,10]],
              [[7,13],[16,20]],
              [[0,12]]]
test = Solution()
for i in range(len(firstList)):
    test.intervalIntersection(firstList[i],secondList[i])
    print(test.intersect)