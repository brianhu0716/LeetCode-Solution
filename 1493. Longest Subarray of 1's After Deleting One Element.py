# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 10:56:58 2021

@author: Brian
"""
'''
本題要求將一個binary array中只移除一個元素，並回傳連續出現1的最長長度，的思路如下：
如果序列中有出現0，那一定可以透過移除一個0使兩相鄰連續出現1的子序列合成長度更長的子序列，但如果序列中連續兩次出現0
則之前的子序列與之後的子序列就不能合成了(因為移除1個0後還有1個0)，因此
(a) 我們用一個c0的變數檢視是否連續出現兩個0，如c0 = 1的話將之前計算的連續1的個數(c1)存到暫存器res中，
    繼續執行，如果下一個元素是1，c0即可清0，如果又是0，此時我們將res中的數字相鄰的兩兩相加，取最大值，代表再出現00
    之前能夠合成的最長1子序列(ex : 00 --> 111011111101,111"0"11111101 --> 111111111)，存入sub_seq1中
(b) 接著我們接res,c1,c0都清0，重複(a)的算法直到又遇到00的情況，並在找到移除一個0的最長長度後存入sub_seq1，直到序列完結
(c) 當遍歷序列後，取sub_seq1中最大的值即為答案(整個序列中移除一個1得到的最長連續1的長度)
*** 由於我們是在遇到0後才統計一次，因此如果最開始的元素nums[0]是1的話，它之前的一段會沒被考慮到，因此跳出while回圈後，如果c0
    是0的話，res要在append(c1)一次，接著更新由index 0 到 00 之間的相鄰兩連續1的子序列長度在移除中間的一個0後得到的新長度
*** 因為一定要移除一個元素，如果我們發現最後取出的連續1的最長長度與元序列長度相等，代表該序列都是1，因此我們將答案減1即可
'''
class Solution:
    def longestSubarray(self, nums) -> int:
        sub_seq1,res = list(),list()
        c0,c1,l = 0,0,len(nums)
        while nums:
            if nums[-1] == 1:
                c1 += 1
                c0 = 0
            else:
                c0 += 1
                if c0 == 2:
                    '''res[i] + res[i + 1] 是計算相鄰兩連續1的子序列長度在移除中間的一個0後得到的新長度，如果res中只有一個元素
                    直接append到sun_seq1即可
                    '''
                    sub_seq1.append(max([res[i] + res[i + 1] for i in range(len(res) - 1)])) if len(res) > 1 else sub_seq1.append(res[-1])
                    c0,c1 = 0,0
                    res = list()
                else:
                    res.append(c1)
                    c1 = 0
                    
            nums.pop()
        if c0 == 0 :
            res.append(c1)
        sub_seq1.append(max([res[i] + res[i + 1] for i in range(len(res) - 1)])) if len(res) > 1 else sub_seq1.append(res[-1])
        return longest1 if ((longest1 := max(sub_seq1)) != l) else longest1 - 1
test = Solution()
nums = [[1,1,0,1],
[0,1,1,1,0,1,1,0,1],
[1,1,1],
[1,1,0,0,1,1,1,0,1],
[0,0,0]]
for num in nums:
    print(test.longestSubarray(num))