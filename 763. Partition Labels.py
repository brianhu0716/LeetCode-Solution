# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 00:02:04 2021

@author: Brian
"""
'''
本題希望能夠在一串字串中盡可能分割成多個子字串，且任一子字串中出現的字不可以在其他子字串中出現，解題的思路如下:
(a) 首先設定起始點i，並將起始點的字設成flag，由字串的後方搜索至起始點，若於位置flag_end出現第一次flag，則計算由
    起始點到flag_end之間所有不為flag的字(otherWord)
(b) 由字串尾部往前搜索至flag_end，若於位置other_max_end第一次出現於otherWord中的字,則我們必須更新therWord為
    出現在flag_end至other_max_end間的字，完成後將flag_end的值更新為other_max_end，重複(b)直到other_max_end為
    -1(小於flag_end)為止，這代表從起始點至flag_end區間中所已有的字都不會再出現在flag_end到字串尾部了，此時我們
    計算字串中由起此點i至flag_end的長度後，更新起始點為flag_end + 1
(c)若步驟(a)中的flag_end的值為-1，代表該flag於字串中只出現一次，基於要最大化分割字串的理由，我們直接將該字切割出來
    並位移1個位置作為新起始點

'''
class Solution:
    def updateMaxIndexfromEnd(self,otherWord,end,start): #  
        for j in range(end - 1,start,-1):
            if self.S[j] in otherWord:
                return j
        return -1
    def partitionLabels(self, S: str):
        i,ls,self.S,partition = 0,len(S),S,[]
        while i < ls:
            flag = self.S[i]
            flag_end = -1
            for j in range(ls - 1,i,-1):
                if self.S[j] == flag:
                    flag_end = j
                    break
            if flag_end != -1:
                otherWord = set(self.S[i] for i in range(i + 1,flag_end))
                while (other_max_end := self.updateMaxIndexfromEnd(otherWord,ls,flag_end)) > flag_end:
                    otherWord = set(self.S[i] for i in range(flag_end + 1,other_max_end))
                    flag_end = other_max_end
                partition += [self.S[i:flag_end + 1]]
                i = flag_end + 1
            else:
                partition += [flag]
                i += 1
        return partition
            



S = ["ababcbacadefegdehijhklij",
      "andnengtyuo",
      "qiejxqfnqceocmy",
      "mlullbhiuiujgvwvurcdvhzdk"]
# S = ['andnengtyuo']
test = Solution()
for s in S:
    ans = test.partitionLabels(s)
    print(ans,[len(s) for s in ans])
    
        