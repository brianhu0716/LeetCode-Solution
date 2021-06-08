# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 08:37:41 2021

@author: Brian
"""
'''
本題關鍵在於與結構中最大高度的位置是無法收集雨水的，因此我們以最大高度位置作為邊界，向後向前搜索邊界位於何處，
而邊界又只能是非0值的位置因此我們先搜索所有的非0值位置，若非0值位置的最小值比最大高度的位置還大，代表前方結構
無法蒐集雨水，反之若非0值位置的最大值比最大高度的位置還小，代表後方無法蒐集雨水
'''
'''
在確定前後邊界時思路為，先設定由後往前的第一個非0值位置作為右邊界，由該點依序向最大高度位置搜索，只要碰到比該
邊界位置的高度小的位置其蒐集雨水的最大面積為(右邊界高度-該位置高度)*寬(=1)，若遇到比右邊界高度更高的位置時，
應將右邊界的位置更新為該點的為值，右邊界值更新為該點的值；如此才能保證蒐集到最多的雨水。依此類推，即可算出
前方結構的最大蒐集雨水面積，結束程式
'''
class Solution:
    def trap(self, height):
        self.imax = height.index(max(height))
        inz = [index for index,value in enumerate(height) if value != 0] # 所有非0的位置
        self.area = 0
        if not inz or inz[-1] == inz[0]: # # 只有一個非0值或沒有非0值-->不可能捕捉雨 
            return self.area
        else:
            if inz[0] <= self.imax: # 如果有非0值位置存在於最大值位置前，則可以收集左半部的雨水
                self.inzl = inz[0]
                self.vnzl = height[self.inzl] 
                self.calculateLeftSide(height)
            if inz[-1] >= self.imax: # 如果有非0值位置存在於最大值位置後，則可以收集右半部的雨水
                self.inzr = inz[-1]       
                self.vnzr = height[self.inzr]
                self.calculateRightSide(height)
        return self.area
        
    def calculateLeftSide(self,height):
        for i in range(self.inzl + 1,self.imax,1):
            if height[i] >= self.vnzl:
                self.inzl = i
                self.vnzl = height[i]
            else:
                self.area += (self.vnzl - height[i]) * 1
    def calculateRightSide(self,height):
        for i in range(self.inzr - 1,self.imax,-1):
            if height[i] > self.vnzr:
                self.inzr = i
                self.vnzr = height[i]
            else:
                self.area += (self.vnzr - height[i]) * 1
        
        
           
arr = [[0,1,0,2,1,0,1,3,2,1,2,1],
          [4,2,0,3,2,5]]
test = Solution()

for i in range(len(arr)):
    test.trap(arr[i])
    print('max rain traped area =',test.area)
    
    