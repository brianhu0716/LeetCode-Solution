# -*- coding: utf-8 -*-
"""
Created on Fri May 21 22:27:13 2021

@author: brian.hu
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s : return 0
        for i in range(n := len(s)) :
            char = s[i]
            if char == " " : continue # might be leading space
                
            elif char == "-" or char == "+" or char.isnumeric() :  # start find number
                start = i # record start position
                for j in range(i + 1,n + 1) :
                    if j == n : 
                        end = n
                        break
                    elif not s[j].isnumeric() : 
                        end = j
                        break
                #print(start,end)
                break
            else : return 0 # meet any char that violates the searching rule
		# "   " -- > all character in string is space(without start position)
		# "+" or "-" -- > invalid expression
        if "start" not in locals() or end - start == 1 and s[start : end] == "-" \
            or s[start : end] == "+" :  
            return 0
        
        num = int(s[start : end])
        return min(num,2 ** 31 - 1) if num >= 0 else max(num,-2 ** 31) 