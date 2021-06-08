# -*- coding: utf-8 -*-
"""
Created on Fri May 21 21:39:04 2021

@author: brian.hu
"""
"""
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(address):
            # IP中的任一address只有兩種可能：
            # 第一 : 如果是leading zero，則只可以是"0"("00","012"...都無效)
            # 第二：數字必須要介於0 ~ 255之間
            if address[0] == "0" and len(address) > 1 : # leading zero且長度大於1
                return False
            
            return True if (0 <= int(address) <= 255) else False
        
        def dfs(idx,s,res,length):
            
            """

            Parameters
            ----------
            idx : TYPE int
                當前的起始位置
            s : TYPE str
                題目給定的字串
            res : TYPE str
                當前狀態的IP表達式
            length : TYPE int
                當前IP的長度

            Returns
            -------
            None.

            """
            if idx == n:
                #print(res)
                if length == 4 : self.ans += [res[:][:-1]]  # 去掉最後一個小數點
                return 
            
            length += 1
            #print("address : ",res)
            for shift in [1,2,3] : # 一個address的長度可能是1 ~ 3位的數字
                if idx + shift - 1 < n :
                    possible = s[idx : idx + shift]
                    #print(possible,length,idx + shift)
                    if valid(possible) and length <= 4 : 
                        # IP中的任以address必須為有效表示且IP總長度必須等於4
                        #print(res,possible,idx + shift)
                        dfs(idx + shift,s,res + possible + ".",length)
            length -= 1            

        self.ans = list()
        n = len(s)
        dfs(0,s,"",0)
        return self.ans