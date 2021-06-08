# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:43:01 2021

@author: -
"""
# 8997,8998
def deal0(n,flag,ln): # 退位找與目標差距最小的值
    i = flag - 1
    (mid := '9') if ln % 2 == 1 else (mid := '99')
    while i >= 1: # 第一位不可能是0
        if n[i] == '0':
            mid += '99'
            i -= 1
        else:
            break
    if i == 0 and n[0] == '1': # 1001,...
        return mid + '9'
    else: # 808,
        return n[:i] + str(int(n[i]) - 1) + mid + str(int(n[i]) - 1) + n[:i][::-1]
def deal9(n,flag,ln): #進位找與目標差最小的值
    i = flag - 1
    (mid := '0') if ln % 2 == 1 else (mid := '00')
    while i >= 1:
        if n[i] == '9':
            mid += '00'
            i -= 1
        else:
            break
    if i == 0 and n[0] == '9' :
        return '1' + mid + '0' +'1'
    else:
        return n[:i] + str(int(n[i]) + 1) + mid + str(int(n[i]) + 1) + n[:i][::-1]
def nearestPalindromic(n) -> str:
    ln = len(n)
    if (nn := int(n)) <= 11:
        return '9' if n == '10' or n == '11' else str(int(n[0]) - 1)
    elif nn >= 12 and nn <= 99:
        if n[0] == n[1]:
            return str(int(n[0]) - 1) * 2 if n != '99' else '101'
        elif int(n[0]) < int(n[1]):
            n1,n2 = n[0] * 2,n[1] * 2
        else:
            n1,n2 = str(int(n[0]) - 1) * 2 , n[0] * 2
        return n2 if abs(int(n2) - int(n)) < abs(int(n1) - int(n)) else n1
    else:  # 考慮長度大於3
        (flag := int((ln - 1) / 2)) if ln % 2 == 1 else (flag := int(ln / 2) - 1)
        if ln % 2 == 1 and n == n[::-1]: # 長度為奇數，回文 # ok
            if n[flag] == '9': 
                n1,n2 = n[:flag] + str(int(n[flag]) - 1) + n[flag + 1:] ,deal9(n, flag, ln)
            elif n[flag] == '0':
                n1,n2 = deal0(n, flag, ln),n[:flag] + str(int(n[flag]) + 1) + n[flag + 1:]
            else:
                n1,n2 = n[:flag] + str(int(n[flag]) - 1) + n[flag + 1:],\
                        n[:flag] + str(int(n[flag]) + 1) + n[flag + 1:]
        elif ln % 2 == 1 and n != n[::-1]: # 長度為奇數，不是回文
            if int((nq := n[:flag + 1] + n[:flag][::-1])) > int(n): # ok
                n2 = nq
                (n1 := deal0(n, flag, ln)) if n[flag] == '0' else \
                    (n1 := n[:flag] + str(int(n[flag]) - 1) + n[:flag][::-1]) 
            else:
                n1 = nq
                (n2 := deal9(n, flag, ln)) if n[flag] == '9' else \
                    (n2 := n[:flag] + str(int(n[flag]) + 1) + n[:flag][::-1]) 
        elif ln % 2 == 0 and n == n[::-1]: # 長度為偶數，回文(ok)
            if n[flag] == '0':
                n1,n2 = deal0(n,flag,ln),n[:flag] + '1' * 2 + n[flag + 2:]
            elif n[flag] == '9':
                n1,n2 = n[:flag] + '8' * 2 + n[flag + 2:],deal9(n, flag, ln)
            else:
                n1,n2 = n[:flag] + str(int(n[flag]) - 1) * 2 + n[flag + 2:],\
                        n[:flag] + str(int(n[flag]) + 1) * 2 + n[flag + 2:]
        else:# 長度為偶數，不是回文(ok)
            if n[flag] < n[flag + 1]:
                n1,n2 = n[:flag + 1] + n[:flag + 1][::-1],\
                        n[:flag] + n[flag + 1] * 2 + n[:flag][::-1] # 因為n[flag]比較小，所以以他為基準+1算大於n的第一個回文值
            elif n[flag] > n[flag + 1]:
                n1,n2 = n[:flag] + n[flag + 1] * 2 + n[:flag][::-1],\
                        n[:flag + 1] + n[:flag + 1][::-1]
            else: # 中間兩個旗標位置值相等
                if n[flag] == '0':
                    n1,n2 = deal0(n,flag,ln),n[:flag] + '1' * 2 + n[flag + 2:]
                elif n[flag] == '9':
                    n1,n2 = n[:flag] + '8' * 2 + n[flag + 2:],deal9(n, flag, ln)
                else:
                    n1,n2 = n[:flag] + str(int(n[flag]) - 1) * 2 + n[flag + 2:],\
                            n[:flag] + str(int(n[flag]) + 1) * 2 + n[flag + 2:]
        print(n1,n2)
        return n2 if abs(int(n2) - int(n)) < abs(int(n1) - int(n)) else n1
# n = ["1235",
#       "12476",
#       "2",
#       "6336",
#       "10",
#       "11",
#       "100",
#       "10001",
#       "10002",
#       "1020201",
#       "102000201",
#       "1890000981",
#       "23",
#       "88",
#       "92",
#       "97",
#       "9"]
n = ["19999"]
for nn in n:
    print('nearest palindrome of',nn, 'is' ,nearestPalindromic(nn))
                    