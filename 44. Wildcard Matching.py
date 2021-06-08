# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 07:23:34 2021

@author: Brian
"""

class Solution:
    def isMatch(self,s,p):
        self.s = s
        self.result = True
        i = 0
        lp = len(p)
        while i <= lp - 1:
            print('處理前的p',p[i:])
            print('處理前的s',self.s)
            if p[i] == '?':
                if not self.s:
                    self.result = False
                    return self.result
                else:
                    self.s = self.s[1:]
                    i += 1
                    print('處理後的s',self.s)
                    print('\n') 
            elif p[i] == '*':
                flag = ''
                nq = 0
                for j in range(i+1,lp):
                    if not flag:
                        if p[j] == '*':
                            i = j
                            continue
                        elif p[j] == '?':
                            i = j
                            nq += 1
                        else:
                            flag += p[j]
                    else:
                        if p[j] == '*' or p[j] == '?':
                            break
                        else:
                            flag += p[j]
                        
                    
                
                if nq != 0:
                    if len(self.s) < nq:
                        self.result = False
                        return self.result
                    else:
                        self.s = self.s[nq:]
                        print('處理後的s',self.s)
                
                if flag:
                    lf = len(flag)
                    repeat = False # p中的flag是否有重複
                    print('*後的字串',flag)
                    '''判斷p中是否有與當前flag一樣的字串'''
                    if j != lp - 1: # 如果flag出現在最後，則無需做重複判斷，防止p = '***a'
                        for k in range(j,lp):
                            if p[k:k+lf] == flag: 
                                repeat = True
                                print('p中是否有重複的flag:',repeat)
                                break
                        
                    ''''更新下一輪p的index值'''
                    if j == lp - 1 and p[j] != '*' and p[j] != '?': # 若p的最後幾個字元都是字，則處理完後直接加1使程式跳出while迴圈
                        i = j + 1
                    else: # 若否，代表p還有其餘字符(* or ?)未被判斷，這時的情況代表找到flag後又遇到?或*，指標需停留在於原處以待下一次判斷
                        i = j
                        

                    ls = len(self.s)
                    lastindex = -1
                    for j in range(0,ls - lf + 1):
                        if lastindex == -1:
                            if self.s[j:j+lf] == flag:
                                lastindex = j
                                if repeat :
                                    break
                               
                        else:
                            for k in range(lastindex + lf,ls - lf + 1,lf):
                                if self.s[k:k+lf] == flag:
                                    lastindex = k

                    
                    if lastindex == -1:
                        self.result = False
                        return self.result
                    else:
                        if lastindex + lf - 1 != len(self.s) - 1: # 如果s中與flag相符的字串尾部索引不等於s的總長度，則扣除前面重疊部分後繼續搜索
                            self.s = self.s[lastindex + lf:]
                        else: # 否則直接將下一個需要判別的索引值設定為空自元，依照之邏輯繼續搜索
                            self.s = ''
                else:
                    # i = j      #  
                    return self.result # p的最後幾個字元都是?或*，且已經確定s剩下的單字足夠抵消?效應，此時無論剩下多少個單字都是true
                print('s中與flag相符的字串的起始位置:',lastindex)
                print('處理後的s',self.s)
                print('下一個索引',i)
                print('\n') 
            else:
                if self.s and self.s[0] == p[i]:
                    self.s = self.s[1:]
                    i += 1
                    print('處理後的s',self.s)
                else:
                    self.result = False
                    return self.result
                print('\n')        
        if not self.s:
            return self.result
        else:
            self.result = False
            return self.result
        
        

answer = []
case = [('aaaa','***a'), # True
        ("adceb","*a*b"), # True
        ('abefcdgiescdfimde',"ab*cd?i*de"), # True
        ("abcabczzzde","*abc???de*"), # True
        ("aab","c*a*b"),  # False
        ("mississippi","m??*ss*?i*pi"), # False
        ("ab","*a*"), # True
        ("mississippi","m*iss*iss*"), # True
        ("aba","*a"), # True
        ("babb","*b*b")] # True
# case = [("mississippi","m*iss*iss*"),] # True
# case = [("babb","*b*b")]
test = Solution()
for i in range(len(case)):
    test.isMatch(case[i][0], case[i][1])
    answer += [test.result]
print(answer)

    

                    
                    
                    
                    
                
                        