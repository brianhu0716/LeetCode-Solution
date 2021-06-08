# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:45:05 2021

@author: Brian
"""
'''
關鍵在於兩時間間隔若大於duration的話，則最大只能提供duration的效果
若小於duration的話則提供兩時間間隔差的效果。當計算到最後一個施放時間點
(timeSeries[-1])時，直接加duration
'''
class Solution:
    def findPoisonedDuration(self, timeSeries, duration) -> int:
        output = 0
        for i in range(l := len(timeSeries)):
            if i == l - 1:
                output += duration
            else:    
                if (diff := timeSeries[i + 1] - timeSeries[i]) < duration:
                    output += diff
                else:
                    output += duration
        return output
    