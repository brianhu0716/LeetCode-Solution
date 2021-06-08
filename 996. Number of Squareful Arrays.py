# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:04:37 2021

@author: brian.hu
"""

"""
本題關鍵：如何避免重複出現的組合
ex: [2,2,2]
1. res = [2] , i = 0,vistted = [T,F,F]
2. res = [2,2] , i = 1,visited = [T,T,F]
3. res = [2,2,2] , i = 2,visited = [T,T,T]
dfs return (self.ans = [[2,2,2]])
4. res = [2,2], i = 3(out for loop bound --> return 2.), visited = [T,T,F]
5. res = [2,2] , i = 2, visited = [T,F,T]
     --> 此時我們發現nums[i] == nums[i - 1],且nums[i - 1]是unvisited的狀態，也就是說step 6.一定
         會拿nums[i - 1](選到相同的答案,出現這種狀況continue,dfs的狀態回到 step 1.)
7. res = [2] , i = 1,visited = [F,T,F]
    --> 同樣的我們又發現nums[i] = nums[i - 1] 且nums[i - 1]是unvisited的狀態，則step 8.一定
        會拿nums[i - 1](選到相同的答案,出現這種狀況continue,dfs的狀態回到 step 7.)
9. res = [2], i = 2,visited = [F,F,T] 與step 7.相同,直接continue
11. res = [] , i = 3(out of for loop bound) dfs 流程完全結束，最後答案中只有(2,2,2)

"""
import math
class Solution:
    def numSquarefulPerms(self, nums) -> int:
        def dfs(nums,res,visited,length):
            if length == n :
                self.ans.add(tuple(res[:])) # 加一組答案
                return 
            
            for i in range(n) :
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: # 重複出現的數字不必在往下搜尋
                    continue
                if not visited[i] and \
                (not res or int(math.sqrt(res[-1] + nums[i])) ** 2 ==  res[-1] + nums[i]) : # 當前數字與前一個數字加起來是完全平方數
                    visited[i] = True
                    res += [nums[i]]
                    print("search :",res,i,visited)
                    dfs(nums,res,visited,length + 1) # dfs
                    visited[i] = False
                    res.pop()
                    print("return :",res,i,visited)
        self.ans = set()
        n = len(nums)
        dfs(sorted(nums),list(),[False for _ in range(n)],0)
        return len(self.ans)
 
Solution().numSquarefulPerms([2,2,2])