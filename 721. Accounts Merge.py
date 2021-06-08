# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:49:15 2021

@author: Brian
"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(name,emails,accounts):
            same_guy = set() # 經確認後為同一人的id
            for email in emails: # emails可能因為搜索到同一人的id而擴張，直到沒有同一人的eamil加入為止
                for idx,account in enumerate(accounts):
                    #    確認不是同一人     當前搜索的人名字至少要一樣  當前搜索的email重複出現在以被歸類為同一人的emails中
                    if idx not in same_guy and account[0] == name and email in account[1:]: 
                        same_guy.add(idx) # 將當前的位置加入合併名單中
                        for email_add in account[1:]: # 將當前的所有email加入同一人的email中
                            if email_add not in emails: # 不可以重複輸入相同的email
                                emails.append(email_add)
            return same_guy,emails
                        
                
        table = []
        while accounts:
            account = accounts.pop() # 選一個account做DFS搜索的參考
            rmv_idx,emails = dfs(account[0],list(set(account[1:])),accounts)
            table.append([account[0]] + sorted(emails))
            for idx in sorted(list(rmv_idx))[::-1]: # 移除被歸類字在同一人的位置
                accounts.pop(idx)
        return table