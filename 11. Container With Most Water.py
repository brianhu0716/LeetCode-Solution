# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 08:08:07 2021

@author: Brian
"""
def searchFirstMaxPair(x,flag,r): # x:域搜尋序列,r:是否反向搜尋,c:計算是否需要移除最大值往下搜尋
    if r == False:
        for i in range(len(x)):
            if x[i] == flag:
                break
        return i
    else:
        for i in range(len(x) - 1,-1,-1):
            if x[i] == flag:
                break
        return i
def searchFirstGreater(x,flag,r):
    if r == True:
        for i in range(len(x) - 1,-1,-1):
            if x[i] >= flag:
                break
        return i
    else:
        for i in range(len(x)):
            if x[i] >= flag:
                break
        return i

# height = [1,8,6,2,5,4,8,3,7]
# height = [1,0,0,0,0,0,0,2,2]
# height = [2,3,4,5,18,17,6]
# height = [2,3,4,5,18,17,6]
# height = [4,3,2,1,4]
# height = [1,2,1]
# height = [1,3,2,5,25,24,5]
height = [0,14,6,2,10,9,4,1,10,3]
lh = len(height)
aloneMax = []
x = sorted(height)
flag = -1
for i in range(lh - 1,0,-1):
    if x[i] != x[i - 1]:
        aloneMax += [x[i]]
    else:
        flag = x[i]
        start = searchFirstMaxPair(height,flag,r = False)
        end = searchFirstMaxPair(height,flag,r = True)
        break
    
area = []
if flag == -1: # 序列中所有的值都是單獨出現無法湊成對
    imax = height.index(max(height))
    l = [i for i in range(lh - 1) if i != imax]
    for i in l:
        if i > imax:
            area += [(i - imax) * height[i]]
        elif i == imax:
            continue
        else:
            area += [(imax - i) * height[i]] # 防止靠長度取勝
    area += [min(height[0],height[-1]) * (lh - 1)]
    print('1最大面積為:',max(area))
else: # 有成對的局部極大值
    maxArea = height[start] * (end - start)
    if aloneMax: # 先把單獨且值比成對極大值更大的可能計算出來(固定其中一個邊為start or end)
        for m in aloneMax:
            i = height.index(m)
            if i > end:
                area += [(i - start) * height[end]]
            elif i < start:
                area += [(end - i) * height[start]]
        
    for i in range(len(aloneMax)): # 獨立值之間的面積也需要考慮
        for j in range(i + 1,len(aloneMax)):
            area += [aloneMax[j] * abs(height.index(aloneMax[i]) - height.index(aloneMax[j]))]

    used = []
    for i in range(0,start): # 接著考慮值比成對極大值小的可能
        if height[i] > height[start] or height[i] in used:
            continue
        else:
            if (end - i) * height[i] > maxArea:
                ref = height[i]
                j = searchFirstGreater(height,ref,r = True)
                if j >= end:
                    area += [(j - i) * height[i]]
                    used += [height[i]]

    used = []
    for i in range(lh - 1,end,-1):
        if height[i] > height[end] or height[i] in used:
            continue
        else:
            if (i - start) * height[i] > maxArea:
                ref = height[i]
                j = searchFirstGreater(height,ref,r = False)
                if j <= start:
                    area += [(i - j) * height[i]]
                    used += [height[i]]
    area += [maxArea]
    print('最大面積為:',max(area))
            


