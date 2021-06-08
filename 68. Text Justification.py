# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:01:30 2021

@author: brian.hu
"""
"""
本題分兩部分：第一、找出每一段最多可以塞多少字。第二、將每段的字以及間隔重新安排後寫入答案
1.主程式為第一部分：
我們每讀到一個字就必須把之前剩餘的位置扣除該字的長度加1(1代表至少要一個空格)，當剩餘的長度不
足以塞入另一個字時，將該段中的字進行排序
2.reshape函式的功能可以對每段中的字以及空白做最佳化：
首先我們要知道當這段有多少字(Nwords)、以及可以被安排的空格數
(Nspace,為該段最多容納的字元數扣掉已經被各字串佔有的位置)，由此我們可以計算出字與字之間的
間隔(spaces)，以及剩餘的間隔數(left)。當間隔不能被均分時，左邊的間隔數必須比右邊多，
因此每當我們放入一個字時，後面跟著的空白數必須是(spaces + 1,1由left中提供，直到left = 0為止)
當我們放入該段最後一個字時，不需要加空白，直接return 
*** 當我們在更新最後一段時，方法為每填入一個字串，後面就跟一個空白鍵，直到填入最後一個字後，
    把剩餘的空白數加到其尾部，即為最終答案

"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def reshape(words_now):
            Nword = len(words_now) 
            Nspace = maxWidth - sum([len(word) for word in words_now])
            if Nword == 1 : return words_now[0] + " " * Nspace 
            
            spaces , left = Nspace // (Nword - 1) , Nspace % (Nword - 1)
            paragraph = ""
            for idx,word in enumerate(words_now):
                paragraph += word
                if idx == Nword - 1 : return paragraph
                if left != 0:
                    paragraph += " " * (spaces + 1)
                    left -= 1
                else:
                    paragraph += " " * (spaces)
                    
        res,ans = list(),list()
        remain = maxWidth
        idx,n = 0,len(words)
        while idx < n :
            word = words[idx]
            if remain > len(word):
                res.append(word)
                remain -= (len(word) + 1)
                idx += 1
            elif remain == len(word): # 該段的字尾，不需要空格
                res.append(word)
                remain -= len(word)
                idx += 1
            else:
                ans.append(reshape(res))
                remain = maxWidth
                res = list()
        
        if res : 
            last_paragraph = ""
            for idx,word in enumerate(res) :
                last_paragraph += word 
                maxWidth -= len(word)
                
                if idx == len(res) - 1 : break
                    
                last_paragraph += " "
                maxWidth -= 1
                
        return ans + [last_paragraph + " " * maxWidth]