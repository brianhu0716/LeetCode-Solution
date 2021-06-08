# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 08:25:12 2021

@author: Brian
"""
'''
CPU執行時是由stack的模式運作，也就是說當有一個project A在運行中，又有另一個project B被呼叫，此時會先執行最近一次被呼叫的
project B，等到project B運行完後才會回到Project A繼續執行，要計算各project所花的時間，必須要有以下概念
(1) 當一個A還沒運行完而B又被插入工作時，A已經運行了start_time B - start_time A的時間了；而當B運行完後B運行了
    end_time B - start_time B + 1的時間(+1是因為一個在終點一個在起點，詳見leetcode說明)，此時start_time A要更新到
    end_time B + 1的時間，接著再計算A運行完的時間 end_time A - start_time A + 1的執行時間
程式設計如下：我們需要兩個stack暫存器，一個堆疊各project的start time，另一個堆疊各project的ID，當我們檢視到當前的log是end時
就直接計算stack_project.pop()的運行時間(t - stack_time.pop()) + 1)，接著把stack_time[-1]的時間改到(t + 1)後繼續運行，直到
所有project運行結束為止


'''
class Solution:
    def findFirstWord(self,item):
        for i in range(len(item)):
            if item[i].isalpha():
                return i
    def exclusiveTime(self, n, logs):
        stack_time,stack_project = [],[]
        time = [0 for i in range(n)]
        for log in logs:
            i = self.findFirstWord(log)
            (t := int(log[i + 6:])) if log[i] == "s" else (t := int(log[i + 4:])) # start time or end time
            p = int(log[:i - 1]) # project id
            if not stack_time: 
                stack_time.append(t) 
                stack_project.append(p) 
            else:
                if log[i] == "s":
                    stack_time.append(t)
                    stack_project.append(p)
                    time[stack_project[-2]] += stack_time[-1] - stack_time[-2]
                else:
                    time[stack_project.pop()] += t - stack_time.pop() + 1
                    if stack_time:
                        stack_time[-1] = t + 1 
        return time
