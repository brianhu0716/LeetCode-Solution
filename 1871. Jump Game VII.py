# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:38:08 2021

@author: Brian Hu
"""

1 variable "cnt" counts the number of achievable index in range [i - maxJump, i - minJump] where i is current index , if cnt > 0, it means we have at least one index can make index i is achievable if s[i] == "0".
2 the sliding window and current index move coherently, so we need to update cnt by checking the achievable index of next sliding window. If dp[i - minJump + 1] is True , we can add cnt by 1 because i - minJump + 1 is in the range of window from the next step. On the other hand, if dp[i - maxJump] is True, we need to subtract cnt by 1 because index i - maxJump is out of window range from the next step

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False for _ in s]
        dp[0] = True
        cnt = 1
        for i in range(minJump, len(s)):
            if (s[i] == "0" and cnt > 0):
                dp[i] = True
            if (i - maxJump >= 0 and dp[i - maxJump] == True):
                cnt -= 1
            if (dp[i - minJump + 1] == True):
                cnt += 1
        return dp[-1]