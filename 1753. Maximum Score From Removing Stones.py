# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:35:51 2021

@author: Brian
"""
'''
本題需要保證每拿走石頭的兩個桶子必須是當前內部石頭是量最多的兩個桶子，因此先對桶子內部的石頭數量做排序
永遠先拿到數第一以第二個桶子的石頭，拿完後重新排序，直到至少兩個桶子都沒石頭為止
(兩個桶子沒石頭:l[1] = 0,三個桶子沒石頭：l[2] = 0)
'''
a = 4
b = 6
c = 6
l = sorted([a,b,c])
if l[2] >= l[1] + l[0]:
    print(l[0] + l[1])
else:
    ans = 0
    while l[2] != 0 and l[1] != 0:
        l[1] -= 1
        l[2] -= 1
        ans += 1
        l = sorted(l)
    print(ans)
        