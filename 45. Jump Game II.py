# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:09:51 2021

@author: Brian
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:51:44 2021

@author: Brian
"""
'''
跳格子遊戲的關鍵在於如何以最少的部署到達終點，因此在搜索下一個位置時，應該優先考慮該位置提供的位移量是否
足夠到達終點，若無法得到該值則次要考量應為在起始點到起始點的位移量範圍內的所有索引值+位移量找出最大的做
為下一次搜尋的起始點。
'''
'''
值得注意的是當有兩個以上的索引值+位移量相同時，直接回傳第一個值的位置即可，因為若該位置值剛好是起始點，
則可
'''
class Solution:
    def jump(self, nums) -> int:
        self.jumpcount = 0
        self.start = 0
        self.end = len(nums) - 1
        while True:
            if len(nums) <= 1:
                return 0
            elif self.start + nums[self.start] >= self.end:
                self.jumpcount += 1
                return self.jumpcount
            else:
                self.findNextStart(nums)
                
            # print('next start = ',self.start)
            
    def findNextStart(self,nums):
        rr = []
        f = False
        for i in range(self.start,self.start + nums[self.start] + 1):
            if nums[i] + i >= self.end: # 到該位置後下一次即可到終點
                self.start = i
                self.jumpcount += 1
                f = True
                break
            else:
                rr += [i]
        if f == False:
            val = [nums[i] + i for i in rr] # val是下一個index可以提供的位移量，因此該值一定要越大越好
            self.start = rr[val.index(max(val))]
            self.jumpcount += 1

                
test = Solution()
list1 = [[2,3,1,1,4], # 2
            [2,3,0,1,4], # 2
            [2,1], # 1
            [0],# 0
            [3,2,1], # 1
            [2,3,1], # 1
            [1,2,1,1,1], # 3
            [4,1,1,3,1,1,1], # 2
            [1,2,3], # 2
            [1,3,2], # 2
            [1,1,1,1], # 3
            [5,9,3,2,1,0,2,3,3,1,0,0], # 3
            [3,4,3,2,5,4,3], # 3
            [10,9,8,7,6,5,4,3,2,1,1,0], # 2
            [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3], # 2
            [9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]] # 3
# list1 = [[9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5]]
result = []
answer = [2,2,1,0,1,1,3,2,2,2,3,3,3,2,2,3]
for i in range(len(list1)):
    test.jump(list1[i])
    result += [test.jumpcount]
print(answer == result)