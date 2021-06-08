# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 09:19:25 2021

@author: Brian
"""
'''
本題目標:計算是否可以栽種所有的花(若左或右已經有花(1)，則該位置不能栽種)
(a) 若不需要栽花(n = 0)，直接return True。
(b) 若只有一個位置，則只有要栽種的花是一顆且該位置剛好沒花(0)才可種，否則return False
(c) 若有兩個位置以上：
    (c.1) 先判斷前兩個位置是否都沒種花，若是則將第1個位置變1，之後從位置2開始判斷
    (c.2)由位置2到倒數第2個位置，判斷當前位置值(i)以及前後一個位置(i - 1,i + 1)值，
         只有在3個值都是0時可以在該位置(i)栽花並將該位置值設為1，跳兩個位置繼續執行(c.2)
    (c.3) 判斷最後兩個位置(-1,-2)，若都是0可再種一株
*** (a),(b)(c)中每做一輪都要判斷n是否降至0，若等於0可提前終止並回傳true,若到最後n > 0則return False

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if not n:
            return True
        elif l == 1:
            return True if flowerbed[0] == 0 and n == 1 else False
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
                if not n :
                    return True
            i = 2
            while i < l - 1:
                if flowerbed[i - 1] == 1 or flowerbed[i + 1] == 1:
                    i += 1
                else:
                    if flowerbed[i] == 0:
                        flowerbed[i] = 1
                        n -=1
                    i += 2
                                
                if not n :
                    return True
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                n -= 1
            return True if not n else False 