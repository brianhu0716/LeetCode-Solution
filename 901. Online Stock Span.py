# -*- coding: utf-8 -*-，
"""
Created on Wed Apr  7 00:04:57 2021

@author: Brian
"""
'''
本題計算一個貨品過去連續幾天的價格比當前價格更低(online)，作法如下
(a)我們先設置一個單調遞減的stack，上面的值一錠都比下面更低(因為如果當天的價格比昨天更低，那就只有連續一天而已)，而當我們遇到當
    價格比stack最頂端的價格更高時，我們必須要往前回推，把之前所有價格低於當天的所有元素都pop出來，並統計次數到過去比當前價格高
    的第一天為止，並把當前價格以及比他低的所有天數存到pop頂端，做為下一次比較的參考標準
*** stacj中的元素型態為[price,count]，price為當前價格，count為過去比他價格更低的連續天數

'''
class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price,1])
            return 1
        
        c = 1 # 自己也算一個
        if price >= self.stack[-1][0]: 
            while self.stack and price >= self.stack[-1][0]:
                c += self.stack.pop()[1]
            self.stack.append([price,c])
            
        else:
            self.stack.append([price,c])
        return c


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

