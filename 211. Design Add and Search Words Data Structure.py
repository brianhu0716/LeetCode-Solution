# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:40:12 2021

@author: brian.hu
"""

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # table的key有26個英文字母,對應的value為dict()
        self.table = {char : dict() for char in string.ascii_lowercase}

    def addWord(self, word: str) -> None: 
        # 找到字首後再以當前word的長度為第二個key值將word存入字典
        word_length = len(word)
        prefix = word[0]
        if word_length not in self.table[prefix]:
            self.table[prefix][word_length] = [word]
        else:
            self.table[prefix][word_length].append(word)
            

    def search(self, word: str) -> bool:
        word_length = len(word)
        
        # 搜尋時先找出模式中不為"."的字母以及對應的位置
        pattern = list()
        for idx,char in enumerate(word):
            if char != ".":
                pattern.append([idx,char])
        # 搜尋26個字母的字典中是否有存放與欲搜尋的字串長度相同的list，
        # 並對該list中存的字串逐一核對是否在指定的index中存在指定的字
        for prefix in string.ascii_lowercase:
            if word_length in self.table[prefix]:
                for candidate in self.table[prefix][word_length]:
                    fit = True
                    for idx,char in pattern :
                        if candidate[idx] != char:
                            fit = False
                            break
                    if fit : return True
            
        return False