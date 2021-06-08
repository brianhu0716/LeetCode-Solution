# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:21:18 2021

@author: brian.hu
"""

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary : # 以差一個字的模式建立字典
            for i in range(0,len(word)) :
                self.dict[word[: i] + "*" + word[i + 1 :]].append(word)
        

    def search(self, searchWord: str) -> bool: # 只要差一字字典中有自且與搜尋字不同，就是差一字的答案
        for i in range(len(searchWord)) :
            pattern = searchWord[ : i] + "*" + searchWord[i + 1 :]
            for built_word in self.dict[pattern] :
                 if built_word != searchWord : return True
        return False