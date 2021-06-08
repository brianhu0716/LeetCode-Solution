# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:37:52 2021

@author: Brian
"""
'''
本題重點：post和user的資料要分開儲存，且在取出貼文時僅限於取出是自己發過或追蹤者發過的貼文
(a) 我們首先建立一個字典，該字典的key為只要有發文過或是追蹤別人ID的user name，而key的內部存放這位user追蹤過的ID，等到我們需要
    提取出他的追蹤者或是本人曾經發過的文時，就以該set內部包含的名稱為基準，如果在set中表示這則貼文可能是他自己或是他追蹤的人
    所發因此我們把這則貼文的ID記錄下來，只要記錄了10個可以立刻回傳
(b) 另一方面只要函數呼叫存取post時，我們一慮將post存入self.post中，等到需要讀取時再根據當前user的追蹤名單來取出適當的貼文
*** 設計時的重點
(a) 只要有ID是貼過文的，我們除了將她的貼文訊息存入post中外，還要初始化他的使用者ID，並默認追蹤自己(set中至少有自己的ID)
(b) 如果有追蹤的要求，也會初始化當前user的使用者ID(如果字典中沒有的話)，並將他的追蹤ID以及"自己ID"存入set中
(c) 當有unfollow的呼叫時，我們先檢查該使用者的名稱是否有在字典中，如果沒有就不需要處理(因為他沒發過文也沒追蹤過人，
    當然不會有unfollow的問題存在)，換句話說，這位user如果被呼叫要取出貼文時，也可以直接忽略掉(因為取貼文僅限於取出是自己發過
    或追蹤者發過的貼文)
總結：在users字典中儲存的user都是曾經自己發過文或是有追蹤別人的ID，因為這些人才會在取貼文時有特定的條件需要滿則

'''
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = dict() # 
        self.post = list()
    def createAccount(self,userId):
        self.users[userId] = set()
        self.users[userId].add(userId) # 自己默認追蹤自己

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users.keys(): self.createAccount(userId) # 把發文者的訊息儲存在users字典中
            
        self.post += [[userId,tweetId]]
            
        return
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users.keys(): return # 沒有follow過，也沒有post過(沒有任何貼文可以取，直接return)
        ret = list() # 取出的貼文ID
        k = 10 # 只取最近的10篇
        follow_list = self.users[userId]
        for i in range(len(self.post) - 1,-1,-1):
            if self.post[i][0] in follow_list: 
                ret += [self.post[i][1]]
                k -= 1
            if k == 0: break
        return ret
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId : return  # 自己取消追蹤自己-->不可能
        
        if followerId not in self.users.keys(): self.createAccount(followerId) # ID沒有在users的資料庫，先初始化
        
        self.users[followerId].add(followeeId) # 加入欲追蹤者的ID
        
        return 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users.keys(): return # 沒有follow就不會有unfollow
        if followeeId in self.users[followerId]: # 移除follow中指定名字
            self.users[followerId].remove(followeeId) 


        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)