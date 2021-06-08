# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:54:08 2021

@author: Brian
"""
'''
本題的關鍵在於若遇到-->[[]...[...[]...]..[]][]，此類括號中又帶括號的格式如何處理。因為每個左括號旁邊
一定有數字，因此我們以堆疊的方式一邊儲存這些數字，一邊統計到目前為止遇到多少個左括號；同時如果
遇到右括號的話，表示這是最內層的[]，必須先做處理成先pop出堆疊內最上方的數字以及左括號對應的位置，
如此一來我們就有欲處理的左右括號位置以及重複次數的值，接者只要依照格式將該密碼解密後取代原本的位置即可。
*** 由於只要出現一對[]就要處理，因此只要當前的左括號統計到0，表示目前的所有的[]都解密完畢，可以將這些
    字串先取出後，從頭開始解密剩餘的密碼，逐次疊加後即可完全解密
*** 最後可能會剩下不帶括號的字串，因此最後回傳值必須加上最終剩餘的字串內的文字
解密流程如下：[..[...[]...]..[].][]ekxs --> [..[........]..[].][]ekxs --> [..............[].][]ekxs
                --> [.................][]ekxs --> [.................][]ekxs 
                --> []ekxs --> ..ekxs (code = ...................) 
                --> ekxs (code = .....................) --> code = .....................ekxs
'''
class Solution:
    def reduction(self,s,end):
        n = self.stack.pop() # 把最接近該組括號的數字提出
        start = self.left_b[-1] - len(n) # 欲解封的字串的起始點(n之所以用文字儲存是避免該數字超過1位)
        replace_word = s[self.left_b.pop() + 1 : end] * int(n) # 將[]內的文字複製n次為即將取代原格式的字串
        s = s.replace(s[start : end + 1],replace_word,1) # 取代該字串
        i = start + len(replace_word) # 定義新的搜尋起點(不需要加1，因為start本身也算一格)
        '''
        print("old start",start)
        print("relace word = ",replace_word)
        print("new string",s)
        print("new start",i)
        '''
        return s,i
    def decodeString(self, s: str) -> str: 
        cnt,i = 0,0 # cnt 為計算到當目前為止出現多少次"[]"的形式,i為當前位置
        self.stack,self.left_b,code = [],[],"" # stack儲存"["旁邊的數字，left_b放到當前位置之前的所有左括號的位置
        while i < len(s):
            if s[i].isnumeric(): 
                n = "" # n儲存當前左括號旁的數字
                while s[i].isnumeric():
                    n += s[i]
                    i += 1
                self.stack.append(n)

            elif s[i] == "[" :
                self.left_b.append(i)
                cnt += 1
                i += 1
                #print("index of left bracket",self.left_b)
            elif s[i] == "]" :
                cnt -= 1 # 出現一對[],左括號總數減1
                s,i = self.reduction(s,i) # 將n[string]的格式展開成string * n 後取代原先的格式
                if cnt == 0: # 此時左括號與右括號的數量完全相等，表示目前為止所有的密碼解封完畢，可以先提出
                    code += s[:i]
                    s = s.replace(s[:i],"",1)
                    i = 0 # 把解封完的字串取出後剩餘的字串再由0開始統計
                    #print("code:",code)
                    
            else :# s[i].isalpha():
                i += 1

        return code + s # s 最後可能剩下沒有[]包住的字，必須補上