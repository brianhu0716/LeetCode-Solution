# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:22:51 2021

@author: brian.hu
"""
"""

"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        l = len(beginWord)
        
        wordList = set(wordList)
        wordList.add(beginWord)
        store = collections.defaultdict(list)
        
        # 將每一個word的所有位置中插入"*"代表可以與該word差一個字的pattern
        for word in wordList : 
            for i in range(l) :
                store[word[ : i] + "*" + word[i + 1 : ]].append(word)
        
        used = set(beginWord) # 因為要求最短路徑，我們不需要同樣的字出現兩次
        dq = deque([beginWord])
        level = 1
        while dq :
            #print(dq,level)
            for count in range(len(dq)) :
                word = dq.popleft()
                
                if word == endWord : return level # 找到終點，回傳最短路徑長度
                
                next_pattern = list() # 把與當前word差一個字的所有pattern都挑出來
                for i in range(l) :
                    next_pattern.append(word[ : i] + "*" + word[i + 1 : ])
                
                for pattern in next_pattern : # 把每一個pattern中的字取出
                    # 如果取出的字沒有用過，我們把該字加入下一輪搜索的dq中，並把該字加入用過的字中
                    for next_possible_word in set(store[pattern]) - used :
                        dq.append(next_possible_word)
                        used.add(next_possible_word)                        
            level += 1 # 沒有找到終點，路徑數加1
            
        return 0