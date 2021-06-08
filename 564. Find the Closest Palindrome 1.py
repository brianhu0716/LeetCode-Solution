# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 07:37:17 2021

@author: -
"""

def nearestPalindromic(n) -> str:
    ln = len(n) - 1
    if n != n[::-1]:
        if ln % 2 == 0:
            n1 = n[:int(ln/2)] + n[int(ln/2)] + n[:int(ln/2)][::-1]
            if int(n1) > int(n): # n = 99998,10000,19824...
                if int(n1) - int(n) == 1: # n = 10000,100...
                    p = str(int(n) - 1)
                else: # n = 19824,12803...
                    p = n1
            else: # n = 17894,12894...
                n2 = n[:int(ln/2)] + str(int(n[int(ln/2)]) + 1) + n[:int(ln/2)][::-1]
                if int(n2) - int(n) > int(n) - int(n1): # n = 12894
                    p = n1
                else: # n = 17894,10002,...
                    p = n2
        
        else:
            if int(n) % 10 == 0: # 10,1000...
                p = str(int(n) - 1)
            else: # 1231,43,...
                if ln == 1: # 43,55...(兩位數)
                    test = [10 * i + i for i in range(2,10)] + [101]
                    diff = int(n) - 11
                    for i in range(len(test)):
                        if abs(test[i] - int(n)) > diff:
                            if i == 0:
                                p = '11'
                            else:
                                p = str(test[i - 1])
                            break
                        else:
                            diff = abs(test[i] - int(n))
                else: # 其餘偶數位數的數字(1231,175830)
                    p = n[:int((ln - 1) / 2) + 1] + n[:int((ln - 1) / 2) + 1][::-1]
    else:
        if ln % 2 == 0:
            if n[int(ln/2)] == '0': # 回文、長度為奇數且中位數 = 0
                i = int(ln/2) - 1
                mid = '9'
                while i >= 0:
                    if n[i] == '0':
                        mid += '99'
                        i -= 1
                    else:
                        break
                if i == 0:
                    p = mid + '9' # 10001
                else:
                    p = n[:i] + str(int(n[i]) - 1) + mid + str(int(n[i]) - 1) + n[:i][::-1] # 102000201
            else: # 回文、長度為奇數且中位數 != 0
                if n == '9' * len(n):
                    p = '1' + '0' * (len(n) + 1 - 2) + '1' 
                else:
                    p = n[:int(ln/2)] + str(int(n[int(ln/2)]) - 1) + n[:int(ln/2)][::-1]
        else:
            if n[int((ln - 1) / 2)] == '0': # 回文、長度為偶數且中位數 = 0
                i = int((ln - 1) / 2) - 1
                mid = '99'
                while i >= 0:
                    if n[i] == '0':
                        mid += '99'
                        i -= 1
                    else:
                        break
                if i == 0:
                    p = mid + '9'
                else:
                    p = n[:i] + str(int(n[i]) - 1) + mid + str(int(n[i]) - 1) + n[:i][::-1]
            else: # 回文、長度為偶數且中位數 != 0
                if n == '9' * len(n):
                    if ln != 0:
                        p = '1' + '0' * (len(n) + 1 - 2) + '1' 
                    else:
                        p = '8'
                
                else:
                    p = n[:int((ln-1)/2)] + str(int(n[int((ln-1)/2)]) - 1)
                    p += p[::-1]
    return p
n = ["1235",
     "12476",
     "2",
     "6336",
     "10",
     "11",
     "100",
     "10001",
     "10002",
     "1020201",
     "102000201",
     "1890000981",
     "23",
     "88",
     "92",
     "97",
     "9"]
for nn in n:
    print('nearest palindrome of',nn, 'is' ,nearestPalindromic(nn))
