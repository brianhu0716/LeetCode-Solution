# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:23:13 2021

@author: Brian
"""
'''
本次計算機只會右加減乘除以及數字出現，不會有小刮號，因此利用一個stack存放由右至左所看到的所有數字，由於我們不希望最後還需要處理
加減的問題，因此當程式遇到"-"號時，我們立刻搜尋它之後出現的數字(此時不需要考慮"-"之後是否有空格，因為用int轉換時空白字元會自動被
忽視)，之後將負號存放到數字中，並將該樹字放入堆疊，如此一來到最後堆疊內部的數字只要求和即可。若中途遇到乘或除，則pop出堆疊最尾
的數字與下一個數字先做運算
*** 值得注意的是除法的部分，如果可以整除，就將商放入堆疊，如果兩數同號，商為正只需要用"//"即可，若兩數異號
則必須將"//"後得到的商 + 1才可以使答案往0縮減。該邏輯等效於利用int(n1 / n2) --> 但這樣做比較慢
'''
class Solution:
    def findLastNumber(self,s,start,ls):
        for i in range(start,ls):
            if not s[i].isnumeric():
                return i
        return ls
    def calculate(self, s: str) -> int:
        stack,idx,ls = list(),0,len(s)
        multiple,division = False,False
        while idx < ls:
            char = s[idx]
            if char.isnumeric() or char == "-":
                (end := self.findLastNumber(s,idx + 1,ls)) if char =="-" else (end := self.findLastNumber(s,idx,ls))
                (num := -int(s[idx + 1:end])) if char == "-" else (num := int(s[idx:end]))
                if not multiple and not division:
                    stack.append(num)
                elif multiple:
                    stack.append(stack.pop() * num)
                    multiple = False
                else:
                    #stack.append(int(stack.pop() / num))
                    
                    if (n1 := stack.pop()) % num == 0: # 整除，不取floor
                        stack.append(n1 // num)
                    else:
                        if (n1 >= 0 and num > 0) or (n1 <= 0 and num < 0): # 兩數同號
                            stack.append(n1 // num)
                        else: # 異號又不能整除時，答案加1
                            stack.append(n1 // num + 1)
                    
                    division = False
                idx = end
            elif char == "+" or char == " " :
                idx += 1
            else:
                (multiple := True) if char == "*" else (division := True)
                idx += 1
            print(stack)
        return sum(stack)
s = "14-3/2"
test = Solution()
print(test.calculate(s))