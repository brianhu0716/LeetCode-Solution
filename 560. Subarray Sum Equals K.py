# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:21:15 2021

@author: Brian
"""
'''
前綴和(Prefix Sum)的概念，前綴和是指由index = 0至index = i(i < len(nums))所累加成的數字組成的數列，此種概念非常適合解
這類序列中有正有負，又要求必須要連續的題型，以此題為例，目標是要找到和為k的子序列個數，因此我們先建立一個由前綴和為key值,
出現次數為value值的表，每當我們計算一次前綴和後我們同時可以查表中是否有出現當前prefixSum - k的key出現，有的話代表prefixSum - k
對應的次數即為出現再prefixSum之前且與prefixSum相差k的連續字序列的個數，答案就可以再不斷更新prefixSum的同時累加prefixSum - k對應
的value後得到。如果希望看到prefixSum - k以及prefixSum出現位置可以參照註解部分的程式碼，再更新完prefixSum的字典後，依次查詢key與
key - k是否成對存在，如果都存在，檢驗key中的idx_b是否有大於key - k中的idx_f，有的話加1;這樣的寫法在初始化字典時先給出{0 : [-1]}
的值，代表在位置-1時前綴和為0
*** 關於初始化值的問題可以參考這的範例nums = [3,...],k = 3，如果不先初始化前綴和為0的位置或次數，答案一定會少算一個因為在index
為0的時候，predixSum為3，對應的prefixSum - k 等於0，如果不先初始化就查無鍵值，直接少加1次正確答案
'''

nums = [1,-1,0]
k = 0
nums = [1,1,1]
k = 2
nums = [1,2,3]
k = 3
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        occur,prefixSum,ans = {0 : 1},0,0 # {0 : 1}的意思是再index = 0之前的前綴和 = 0,出現一次
        for num in nums:
            prefixSum += num
            ans += occur.get(prefixSum - k,0) # 一定要先計算prefixSum - k的個數，避免k = prefixSum = 0的狀況會出現錯誤
            occur[prefixSum] = occur.get(prefixSum,0) + 1
        return ans
        '''
        occur,prefixSum,ans = {0 : [-1]},0,0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum not in occur.keys():
                occur[prefixSum] = [i]
            else:
                occur[prefixSum].append(i)
        for key in occur.keys():
            if key - k in occur.keys():
                for idx_b in occur[key]:
                    for idx_f in occur[key - k]:
                        if idx_b > idx_f:
                            ans += 1
        return ans
        '''
        