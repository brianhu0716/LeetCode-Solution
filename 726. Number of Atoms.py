# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:29:16 2021

@author: Brian
"""
'''
由於化學式的寫法都是Na(K2(OH)4)7這類型式，因此在統計時，一定是由後往前看才可以算出最裡層()內原素的總個數
因此在撰寫時依樣採用堆疊的形式由後往前將看到的數字儲存，只要遇到英文字我們就在往前找直到出現大寫為止(
因為元素都是大寫開頭)，找到一個元素後立刻更新字典，該元素出現的次數為stack中所有的數字相乘。值得注意的是
如果遇到"("，必須將stack中最上方的數字剔除，該數字代表內層括號內部的元素乘數，既然由後往後前更新，這些元素
一定已經被統計過，故不需要這個數字做計算了
*** 值得注意的是可能有單一元素出現N次的情況(C2,K4...)，這時因為沒有括號當作基準，因此我們在判定數字的同時
    會在結尾處判別下一個字是否是alpha(英文字母)，如果是的話以變數single來顯示前方這個元素在更新完字典後
    必須先pop掉一個數字，這個乘數只對該元素有效，不能讓它影響到後面判斷次數的程式
'''
class Solution:
    def update_dict(self,element):
        n = 1
        if self.stack:
            for i in self.stack:
                n *= i
        if self.single: # 如果該數字旁邊沒有")"直接是元素，代表該乘數只對單一元素有效，用過後要pop()掉
            self.stack.pop()
            self.single = False
        self.d[element] = self.d.get(element,0) + n
        
    def countOfAtoms(self, formula: str) -> str:
        self.stack,self.d = [],{}
        i,self.single = len(formula) - 1,False
        while i >= 0:
            if formula[i].isnumeric():
                n,digt = 0,0
                while formula[i].isnumeric():
                    n += 10 ** digt * int(formula[i]) # 將讀到的文字轉成數字
                    i -= 1
                    digt += 1
                self.stack.append(n)
                if formula[i].isalpha(): # K4
                    self.single = True # 乘數只對單一元素有效

            elif formula[i].isalpha():
                element = ""
                while formula[i].isalpha():
                    element = formula[i] + element
                    if formula[i].isupper(): # 元素一定是大寫開頭
                        i -= 1
                        break
                    else:
                        i -= 1
                self.update_dict(element)
            elif formula[i] == "(" : # 看左括弧代表最近的乘數已經失效，要從stack中pop掉
                self.stack.pop() if self.stack else self.stack
                i -= 1
            else:
                i -= 1
        ans = ""
        for key in sorted(self.d.keys()): # key : 元素名；d[key] : 出現次數(如果出現一次，不用顯示)
            (ans :=  ans + key + str(self.d[key])) if self.d[key] > 1 else (ans := ans + key)
        return ans
        
formula = ["H2O",
           "Mg(OH)2",
           "K4(ON(SO3)2)2",
           "Be32",
           "(H)"]
# formula = ["(H)"]
test = Solution()
for i in range(len(formula)):
    print(test.countOfAtoms(formula[i]))

