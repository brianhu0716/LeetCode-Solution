# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:42:09 2021

@author: Brian
"""
queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
d = {i : [] for i in range(8)}
for cord in queens:
    dist = (cord[0] - king[0]) ** 2 + (cord[1] - king[1]) ** 2
    if cord[0] == king[0] :
        if cord[1] > king[1]:
            d[0] += [[dist] + cord]
        else:
            d[1] += [[dist] + cord]
    elif cord[1] == king[1]:
        if cord[0] > king[0]:
            d[2] += [[dist] + cord]
        else:
            d[3] += [[dist] + cord]
    elif abs(cord[0] - king[0]) == abs(cord[1] - king[1]):
        if cord[0] < king[0] and cord[1] > king[1]:
            d[4] += [[dist] + cord]
        elif cord[0] > king[0] and cord[1] > king[1]:
            d[5] += [[dist] + cord]
        elif cord[0] < king[0] and cord[1] < king[1]:
            d[6] += [[dist] + cord]
        else:
            d[7] += [[dist] + cord]
    else:
          continue
ans = list()
for key in d.keys():
    if d[key]:
        imax = (res := [val[0] for val in d[key]]).index(min(res))
        ans += [d[key][imax][1:]]
