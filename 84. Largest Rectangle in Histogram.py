# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:06:25 2021

@author: Brian
"""
'''
最初想法：最初我們希望能夠在遍歷程式時，只要發現當前的值大於下一個位置的值時，就直接往下找，直到出現小
於當前高度的位置作終點，但這樣的做法有兩個缺點：
(1) 在當前位置與出現小於當前位置值之間的所有位置都還要再遍歷一遍直到找到比他們小的位置為止，之間的搜索
    過程會與第一次搜索重複
(2) 在找到比當前的值還要小的位置後，我們除了更新當前位置的舉行面積外同時也可以更新停止位置到當前位置的
    矩形面積(因為到當前位置間的所有高度都比停止位置大)，但我們不知道當前位置之前的值是否還能再使矩形
    面積擴張，如果當前位置之前的高度比剛前位置大，則一定可以；若比當前位置小但又比停止位置大，也可以更新；
    但若比停止位置小則不能更新，如此一來程式會變得非常複雜，且演算法難以實現
最好的做法：利用stack
演算流程：建構一個單調遞增的stack，其中累積得值是序列中，所有比前一個位置高度要高的index，如此一來當我們
            遍歷到當前位置值比stack頂端位置值小時，這個值的index就做為更新之前比這個值大的所有位置的"右邊界"
(a)只要當前位置值比之stack頂部位置值小，我們就將stack頂部的值pop出來，提取出對應的高度再乘以當前位置(ind)
    減去stack頂部的位置(stack[-1])再減去1作為寬度(減1是因為頭尾的index都不包含)，計算出面積該位置能畫出的
    最大矩形面積。重複上步驟直到stack頂部的位置的對應值比當前位置值小後將當前位置放入stack頂部，維持stack
    的遞增性
*** 值得注意的是，頂部位置被pop()完後新的頂部位置一定是pop出的位置的左邊界，因為這個位置對應的值一定比
    pop出的位置對應的值小(我們放入stack的邏輯是比stack頂部位置對應的值大才放入)
*** 當前位置被放入後是下一次找到比它小的為值作左邊界才開始計算面積，也就是說當次的操作是以它做邊界去更
    新前面比它大的值的面積
(b)如果當前位置值比stack頂部位置對應的值還要大，則將當前的位置既須堆入stack頂部


'''

class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1] # 先放入一個pseudo-index，作為更新時繼序列最後一個元素的指標
        heights.append(0) # pseudo-value(他的高度一定比任一真實值還要小，所以選0)，在實際序列尾部插入
        max_area = 0
        for ind,val in enumerate(heights):
            if val >= heights[stack[-1]] :
                stack.append(ind)
            else:
                while stack and heights[stack[-1]] > val :
                    min_height = heights[stack.pop()]
                    max_area = max(max_area,min_height * (ind - stack[-1] - 1))
                stack.append(ind)
        return max_area
heights = [[2,1,5,6,2,3],
           [4,2,0,3,2,5],
           [2,1,5,6,2,1]]
test = Solution()
for h in heights:
    print("max area =",test.largestRectangleArea(h))