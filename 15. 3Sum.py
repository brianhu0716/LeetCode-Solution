# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:45:02 2021

@author: Brian
"""
'''
固定第一個值，第二個值由第一個值的右邊開始搜尋，同時右邊界由l - 1開始搜索，為序列已經被sort過，只要三個值相加比0大，
右邊界就往左移一個位置，如果相等就把三個數字加入答案，同時右邊界再減1；如果已經做到三個數字相加都小於0了，就break
且右邊界不動，第二個數字往右一格繼續搜索
*** 因為數列已經由小到大排序,因此第一個數字被固定的情況下，只要第二個數字依序往右移動，需要的第三個數字一定會不斷的往左移，
直到右邊界小於左邊就後終止，接著將第一個數字右移(右邊界一樣從l - 1開始左移)，此時如果發現當前的第一個數字與之前的一樣，
可以跳過繼續下一個判斷(因為當前的結果一定與前一次相同)
*** 用set存答案是避免[-10,-8,-8,-8,0,2,18,18,20] 這種有重複的數字造成答案重複的情況，如果要改用list儲存，程式如最下方所述
只要當rp被更新後的值與上一個值相等，就要不斷往左移值到不等為止；第二個數字也是如此，如果發現右移一個後的值與上一個值一樣，
就繼續往右移，直到數字不同為止(但這種方法程式運行時間長很多，原因不明)

'''
class Solution:
    def threeSum(self, nums): # -> List[List[int]]:
        nums,l = sorted(nums),len(nums)
        ans = set()
        if not nums or nums[0] > 0 or nums[-1] < 0:
            return []
        for i in range(l):
            if i > 0 and nums[i] == nums[i - 1]: # 後面的字與前面重複
                continue
            else:
                ref = nums[i]
                rp = l - 1
                for lp in range(i + 1,l):
                    while lp < rp:
                        if ref + nums[lp] + nums[rp] == 0:
                            ans.add((ref,nums[lp],nums[rp]))
                            rp -= 1
                            break
                        elif ref + nums[lp] + nums[rp] > 0:
                            rp -= 1
                        else :
                            break
                    '''
                    while rp != l - 1 and rp > lp and nums[rp] == nums[rp + 1]:
                        rp -= 1
                    '''
                    
        return ans
            



'''
class Solution:
    def threeSum(self, nums): # -> List[List[int]]:
        nums,l = sorted(nums),len(nums)
        #ans = set()
        ans = list()
        if not nums or nums[0] > 0 or nums[-1] < 0:
            return []
        for i in range(l):
            if i > 0 and nums[i] == nums[i - 1]: # 後面的字與前面重複
                continue

            ref = nums[i]
            rp = l - 1
            for lp in range(i + 1,l):
                if lp > i + 1 and nums[lp] == nums[lp - 1]:
                    continue
                while lp < rp:
                    if ref + nums[lp] + nums[rp] == 0:
                        #ans.add((ref,nums[lp],nums[rp]))
                        ans.append([ref,nums[lp],nums[rp]])
                        rp -= 1
                        break
                    elif ref + nums[lp] + nums[rp] > 0:
                        rp -= 1
                    else :
                        lp += 1
                        break

                while rp != l - 1 and rp > lp and nums[rp] == nums[rp + 1]:
                    rp -= 1
                    
        return ans
'''
