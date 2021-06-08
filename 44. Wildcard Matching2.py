# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:57:21 2021

@author: Brian
"""

class Solution():
    def isMatch(self,s,p):
        self.s = s
        self.lp = len(p) 
        self.i = 0
        self.judge = True
        while self.i <= self.lp - 1:
            if p[self.i] == '?':
                print('1')
                self.dealQ()
                self.i += 1
            elif p[self.i] == '*':
                print('2')
                if self.i == self.lp - 1:
                    return True
                else:
                    self.i += 1
                    self.dealS(p)
            else:
                print('3')
                self.dealL(p)
                self.i += 1                  
                
        if not self.s:
            return True
        else:
            return False
                
    def dealQ(self):
        if self.s:
            self.s = self.s.replace(self.s[0],'',1)
        else:
            return False
    def dealS(self,p):
        
        flag = ''
        nq = 0
        for j in range(self.i,self.lp):
            if flag =='': 
                if p[j] == '?':
                    nq += 1
                elif p[j] == '*':
                    continue
                else:
                    flag += p[j]
                self.i += 1
            else:
                if p[j] != '?' and p[j] != '*':
                    self.i += 1
                    flag += p[j]
                else:
                    break
                
        if nq != 0:
            if len(self.s) < nq:
                # self.judge = False
                return False
            else:
                self.s = self.s[:nq]
                # self.s = self.s[nq:]
        
        if flag != '':
            lastindex = -1
            for j in range(0,len(self.s) - len(flag) + 1,len(flag)):
                '''必須確保多組重復的字串是連續的ex:'abcabczzz...'而不可以是'aca..' '''
                if lastindex == -1: 
                    if self.s[j:j+len(flag)] == flag:
                        lastindex = j

            if lastindex != -1:
                self.s = self.s[lastindex+len(flag):]
            else:
                return False
    def dealL(self,p):
        if self.s and self.s[0] == p[self.i]:
            self.s = self.s.replace(self.s[0],'',1)
        else:
            return False
            

s = "aab"
p = "c*a*b"            
test = Solution()
# test.isMatch(s, p)          
'''

1256 / 1811 test cases passed.
Status: Wrong Answer
Submitted: 0 minutes ago
Input:
"aab"
"c*a*b"
Output:
true
Expected:
false
'''