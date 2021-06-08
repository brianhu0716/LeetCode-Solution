# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 20:54:53 2021

@author: Brian
"""
"""
每次呼叫給定一段時間[start,end),如果這段時間沒有被預訂則加入schedule中並回傳True，否則回傳False
(a) 我們的做法為先判斷schedule中是否為空，若是空的則將[start,end]加入schedule
(b) 接著判斷當前事件的end是否小於等於schedule[0][0]，若是將[start,end]插入schedule[0]，回傳True
(c) 接著判斷當前事件的start是否大於等於schedule[-1][1]，若是將[start,end]插入schedule[-1]，回傳True
(d) 最後我們遍歷整個schedule，如果發現當前的[start,end]滿足start >= self.schedule[i][1] 且 end <= self.schedule[i][0]，
    則將[start,end]插入schedule的i + 1位置中，並回傳True。若遍歷完成後沒有回傳代表當前[start,end]與既定行程時間有衝突，return False
    
"""
class MyCalendar:

    def __init__(self):
        self.schedule = list()

    def book(self, start: int, end: int) -> bool:
        if not self.schedule:
            self.schedule.append([start,end])
            return True
        
        if end <= self.schedule[0][0]:
            self.schedule.insert(0,[start,end])
            return True
        
        if start >= self.schedule[-1][1]:
            self.schedule += [[start,end]]
            return True
        
        for i in range(len(self.schedule)):
            if start < self.schedule[i][0] : # 提前終止
                return False
            elif start >= self.schedule[i][1] and end <= self.schedule[i + 1][0]:
                self.schedule.insert(i + 1,[start,end])
                return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)