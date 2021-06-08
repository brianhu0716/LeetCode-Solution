# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:05:59 2021

@author: Brian
"""
'''
解題思路：將所有的數字都組成一個list(seq)並存取對應的原始list編號(group)，之後在依次搜索最小涵蓋範圍
(a) 首先我們先初始化字典，該字典畢斯包含原先各list中的數字至少一個，接著取最大index作為上界(finish),
    而最小index作為下界(start)
(b) 之後每一次搜索只要由原始上界後找到第一個原始下界對應的編號後，將該index設定為新上界，同時在過程
    中不斷更新各list編號對應的index,照到最小值作為新下界，直到上界到達最大長度為止
'''
class Solution:
    def smallestRange(self, nums):
        n = len(nums)
        seq ,group = [],[]
        for i in range(n):
            seq += nums[i]
            group += [i] * len(nums[i])
        # print(group,seq)
        group = [group[i] for (v,i) in sorted((v,i) for (i,v) in enumerate(seq))]
        seq = [v for (v,i) in sorted((v,i) for (i,v) in enumerate(seq))]
        # print(group,seq)
        r,finish,start = self.findFirstRange(seq,group,n)
        SmallestRange = [seq[start],seq[finish]]
        
        while finish < len(group) - 1:
            r,finish,start = self.findLost(seq,group,start,finish,r)
            if seq[finish] - seq[start] < SmallestRange[-1] - SmallestRange[0]:
                SmallestRange[0],SmallestRange[-1] = seq[start],seq[finish]
            print(SmallestRange)
            print(start,finish)
            print('\n')

        return SmallestRange
        
    def findFirstRange(self,seq,group,n):
        dict1 = {}
        for i in range(len(group)):
            dict1[group[i]] = i
            if len(dict1) == n:
                break
        finish,start = i,min(dict1.values())
        print(dict1,len(dict1))
        return dict1,finish,start
    def findLost(self,seq,group,start,finish,dict1):
        flag = group[start]
        for i in range(finish + 1,len(group)):
            dict1[group[i]] = i
            if group[i] == flag:
                break
        start,finish = min(dict1.values()),i
        return dict1,finish,start
nums = [[-59,-37,-12,39,83,83,83,84],[-38,40,64,75,86,87,89,90],[-4,9,41,57,69,71,72],[-8,13,24,27],[18]]
# nums = [[11,38,83,84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]
test = Solution()
print('smallest range is',test.smallestRange(nums))