# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 07:23:34 2021

@author: Brian
"""

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
            print('p index = ',self.i)
            if p[self.i] == '?':
                print('1')
                self.dealQ()
                self.i += 1
                
                if self.judge == False:
                    print(self.s)
                    return self.judge
                
                print(self.s)
            elif p[self.i] == '*':
                print('2')
                if self.i == self.lp - 1:
                    return self.judge
                    #return True
                else:
                    self.i += 1
                    self.dealS(p)
                    
                    if self.judge == False:
                        print(self.s)
                        return self.judge

                
            else:
                print('3')
                self.dealL(p)
                self.i += 1                  
                print(self.s)
                if self.judge == False: 
                    return self.judge
                
                
        if self.s:
            print('4')
            self.judge = False
            print(self.s)
            return self.judge
        else:
            print(self.s)
            return self.judge
                
    
    def dealQ(self):
        if self.s:
            self.s = self.s.replace(self.s[0],'',1)
        else:
            self.judge = False
            return 
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
                self.judge = False
                return
            else:
                # self.s = self.s[:nq]
                self.s = self.s[nq:]
        
        if flag != '':
            print('flag is',flag)
            lastindex = -1
            for j in range(0,len(self.s) - len(flag) + 1):
                '''必須確保多組重復的字串是連續的ex:'abcabczzz...'而不可以是'aca..' '''
                if lastindex == -1 and self.s[j:j+len(flag)] == flag:
                    lastindex = j
                elif lastindex != -1 and self.s[j:j+len(flag)] == flag:
                    if j - lastindex == len(flag):
                        lastindex = j
                    else:
                        break

            if lastindex != -1 :     
                print('last index = ',lastindex)
                if lastindex != len(self.s):    
                    self.s = self.s[lastindex+len(flag):]
                else:
                    return
                print(self.s)
            else:
                self.judge = False
                return 
    def dealL(self,p):
        if self.s and self.s[0] == p[self.i]:
            self.s = self.s.replace(self.s[0],'',1)
        else:
            self.judge = False
            return
            
            

# s = "aab"
# p = "c*a*b"           
s = "abcabczzzde"
p = "*abc???de*"

# s= 'abefcdgiescdfimde'
# p = "ab*cd?i*de"
# s = 'aaaa'
# p = '***a'
test = Solution()
test.isMatch(s, p)
test.judge
'''

1503 / 1811 test cases passed.
Status: Wrong Answer
Submitted: 0 minutes ago
Input:
"abcabczzzde"
"*abc???de*"
Output:
false
Expected:
true
'''