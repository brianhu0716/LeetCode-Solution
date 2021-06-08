# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:34:12 2021

@author: brian.hu
"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def isValid(before,now,l_word): # 檢查是否差一個單字
            n_diff = 0
            for i in range(l_word):
                if now[i] != before[i]:
                    n_diff += 1
                    if n_diff > 1 : return False
            return True
                
        endWord_exist = False
        neighbors = collections.defaultdict(set)
        l_word = len(beginWord)
        if beginWord not in wordList :
            wordList.append(beginWord)
        
        for i in range(n := len(wordList)) :
            word = wordList[i]
            if word == endWord : endWord_exist = True
            for j in range(n) :
                if i == j or wordList[j] in neighbors[word] : continue
                
                if isValid(word,wordList[j],l_word) :
                    neighbors[word].add(wordList[j])
                    neighbors[wordList[j]].add(word)

        ans = list()
        if not endWord_exist : return ans # 目標不在，提前終止
        
        # 利用BFS逐層擴大範圍搜索，直到找到目標為止
        dq = deque([[beginWord]])
        used = set()
        while dq and not ans :  
            for count in range(len(dq)) :
                path = dq.popleft()
                if path[-1] == endWord :
                    if not ans or len(ans[-1]) == len(path) :
                        ans.append(path[:])
                else :
                    used.add(path[-1])
                    
                for next_node in neighbors[path[-1]] :
                    if next_node not in used :
                        dq.append(path + [next_node])
        return ans