# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:18:22 2021

@author: Brian
"""
'''
本題與54.Spiral Matrx概念相同
'''
class Solution:
    def generateMatrix(self, n):
        lrow,lcol = n,n
        i,j = 0,0
        frow,fcol = True,False
        ci,cj = 0,0
        num = 1
        matrix = [[0 for j in range(n)] for i in range(n)]
        while i != lrow and j != lcol:
            if frow == True and fcol == False:
                if ci % 2 == 0:
                    for k in range(j,lcol):
                        matrix[i][k] = num
                        num += 1
                    i += 1
                else:
                    for k in range(lcol - 1,j - 1, - 1):
                        matrix[lrow - 1][k] = num
                        num += 1
                    lrow -= 1
                frow,fcol = False, True
                ci += 1
            else:
                if cj % 2 == 0:
                    for k in range(i,lrow):
                        matrix[k][lcol - 1] = num
                        num += 1
                    lcol -= 1
                else:
                    for k in range(lrow - 1,i - 1,-1):
                        matrix[k][j] = num
                        num += 1
                    j += 1
                frow,fcol = True,False
                cj += 1
        return matrix
                
            