# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:31:15 2021

@author: Brian
"""
'''
本題希望能找出在給定一系列專案需要的本金(Capital)以及獲得利潤(Profits)的條件下，給定最初的本金(W)以及最多可執行專案的次數(k)，
希望能在執行k次專案後能使累積的本金(W)最大化，限制條件為：
1.當擁有的本金(W)小於執行專案的本金(Capital[i])時，該專案不能被執行
2.任一專案都只能被執行一次
解題思路如下:
(a) 因為選擇專案會被本金所影響，因此我們每挑選一次專案前都先檢查一次剩餘專案中需要最多本金的值，若該值小於所擁有的
    本金W，則我們進一步考慮剩餘可執行的次數k是否大於等於專案數：
    注意:此時已經不受執行專案的本金限制了
    (a.1)若k大於等於剩餘專案數，則直接做完剩餘所有的專案即可獲得最多的利潤
    (a.2)若k小於剩餘專案數，則每次都挑選獲利最大的專案執行並累加本金
(b) 若有任一專案所需的執行本金比所擁有的本金大，則我們一次挑選出可執行的專案，並比較每一個專案可獲得的利潤，
    選出可執行且獲利最大的專案依次執行，並刪除已經完成的專案對應的本金以及利潤值
'''
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits, Capital) -> int:
        while k > 0 and Capital:
            max_cap = max(Capital) # 先計算出需要多少本基金可以不受限制的選擇計畫
            if W >= max_cap:
                if k >= len(Capital):
                    W += sum(Profits)
                else:
                    for i in range(k):
                        W += Profits.pop((i := Profits.index(max(Profits)))) #做完該專案後要刪除
                break
            else:
                imaxp = float('-inf')
                for i in range(len(Capital)):
                    if W >= Capital[i]:
                        if imaxp == float('-inf'):
                            imaxp = i
                        else:
                            if max(Profits[imaxp],Profits[i]) == Profits[i]:
                                imaxp = i
                if imaxp != float('-inf'): #做完該專案後要刪除
                    W += Profits.pop(imaxp)
                    Capital.pop(imaxp)
                    k -= 1
                else: # 若本金不足以做完剩餘的任一專案，則中斷
                    break
        return W
test = Solution()
k,W,Profits,Capital = [[2],[50000]],[[0],[50000]],[[1,2,3],[i for i in range(50000)]],[[0,1,1],[i for i in range(50000)]]
for i in range(len(k)):
    print('max capital = ',test.findMaximizedCapital(k[i][0],W[i][0],Profits[i], Capital[i]))