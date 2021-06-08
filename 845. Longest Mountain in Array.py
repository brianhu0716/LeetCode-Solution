# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:57:37 2021

@author: Brian
"""
'''
先判斷左邊界是否存在，如果存在才找右邊界。左邊界找法為判斷是否第一次出現單調遞增，如果是則更新左邊界值(lp)，如果持續單調遞增，
城市不斷往右搜索，但左邊界不可以變動；等到找到第一次出現單調遞減時，程式開始搜尋第一個違反單調遞減的位置(rp)，最後的長度為rp - lp
下一次開始搜尋的位置為右邊界減1，讓程式可以由下一輪判斷更新左邊界值。如果程式運行到最後一個index(l - 1)都沒有違反單調遞減，則
我們把最後的右邊界改為(l)，以滿足計算長度的數學式(rp - lp)，完成後回傳答案，避免index超出限制
'''
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i,l = 0,len(arr)
        lp_fixed,rp,max_len = False,0,0
        while i < l - 1 :
            if arr[i] < arr[i + 1]:
                if not lp_fixed:
                    lp = i
                    lp_fixed = True
                i += 1
            elif arr[i] > arr[i + 1]:
                if lp_fixed: # 已經有左邊界(之前有發生單調遞增)
                    before = arr[i]
                    for rp in range(i + 1,l): # rp為大於前一個值的index
                        if arr[rp] < before:
                            if rp == l - 1: # 如果到最後一個值都滿足單調遞減，將rp設在l(以滿足判斷長度的數學式rp - lp)
                                rp = l
                                break
                            before = arr[rp]
                        else:
                            break
                    max_len = max(max_len,rp - lp)
                    if rp == l : # 先回傳結果，以免i超出邊界
                        return max_len
                    i = rp - 1
                    lp_fixed = False
                else: # 沒有lp(遇到單調遞減，如:[3,2,1...])
                     i += 1 
            else: # 遇到連續相等的數列([2,2,2])，之前的lp就不算數，必須再往之後找新的lp
                i += 1
                lp_fixed = False
        return max_len