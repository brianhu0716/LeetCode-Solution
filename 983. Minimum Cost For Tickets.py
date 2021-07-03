# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 21:33:57 2021

@author: Brian Hu
"""
'''
dp[i] is the minima cost needs to pay from days[0] to days[i].
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def trackback(start, days, costs):
            now = days[start]
            res = [costs[1], costs[2]]
            flag = False
            for i in range(start, -1, -1):
                if now - days[i] + 1 > 7 and not flag:
                    res[0] = dp[i] + costs[1]
                    flag = True
                elif now - days[i] + 1 > 30:
                    res[1] = dp[i] + costs[2]
                    break
            return min(res)
        dp = [0 for _ in days]
        dp[0] = min(costs)
        for i in range(1, len(days)):
            dp[i] = min(dp[i - 1] + costs[0], trackback(i, days, costs))
        return dp[-1]