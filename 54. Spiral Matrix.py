# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:19:10 2021

@author: Brian
"""
'''
spiral_matrix(螺旋矩陣)的重點在於四個邊的更新都遵循以下規則(把最外圍的邊界往內壓):
    1.順向讀取row(左到右):
        row固定，j由初始位置走到最終位置-->完成後將row的初始位置(i)+1，將row以及col的旗標(frow,fcol)反轉，
        並將更新讀取row的次數的旗標(ci)+1(方便判斷讀取row時是順向或逆向)
    2.順向讀取col(上到下):
        col固定，i由初始值走到最終位置-->完成後將col的末尾位置(lcol)-1，將row以及col的旗標(frow,fcol)反轉，
        並將更新讀取col的次數的旗標(cj)+1(方便判斷讀取col時是順向或逆向)
    3.逆向讀取row(右到左):
        row固定，j由末尾位置走到初始位置-->完成後將row的末尾位置(lrow)-1，將row以及col的旗標(frow,fcol)反轉，
        並將更新讀取row的次數的旗標(ci)+1(方便判斷讀取row時是順向或逆向)
    4.逆向讀取col(下到上):
        col固定，i由末尾位置走到初始位置-->完成後將col的初始位置(j)+1，將row以及col的旗標(frow,fcol)反轉，
        並將更新讀取col的次數的旗標(cj)+1(方便判斷讀取col時是順向或逆向)
******** 若ci以及cj除以2整除:代表現在是順向讀取row以及col，反之代表逆向
******** 終止條件為當row的初始位置與末尾位置重疊或是col的初始位置與末尾位置重疊，跳出while 迴圈X。
            (a)若row的初始位置與末尾位置先重疊-->lcol > lrow
            (b)若col的初始位置與末尾位置先重疊-->lcol < lrow
'''
class Solution:
    def spiralOrder(self,matrix):
        frow,fcol = True,False
        i ,j = 0,0 # i,j分別為row以及col的起始位置
        ci,cj = 0,0
        lrow,lcol = len(matrix),len(matrix[0]) # lrow,lcol分別為row以及col的最終位置
        spiral_matrix = []
        while True:
            if frow == True and fcol == False:
                if ci % 2 == 0:
                    for k in range(j,lcol):
                        spiral_matrix += [matrix[i][k]]
                    i += 1

                else:
                    for k in range(lcol - 1,j - 1,-1):
                        spiral_matrix += [matrix[lrow - 1][k]]
                    lrow -= 1

                ci += 1
                frow,fcol = False,True

            elif frow == False and fcol == True:
                if cj % 2 == 0:
                    for k in range(i,lrow):
                        spiral_matrix += [matrix[k][lcol - 1]]
                    lcol -= 1
                else:
                    for k in range(lrow - 1,i - 1,-1):
                        spiral_matrix += [matrix[k][j]]
                    j += 1

                cj += 1
                frow,fcol = True,False

            if j == lcol or i == lrow:
                break
        return spiral_matrix