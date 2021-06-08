# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 08:11:14 2021

@author: Brian
"""
import numpy as np
a = [0,4,5,10]
pairs = []
diff = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        pairs += [(a[i],a[j])]
        diff += [a[j] - a[i]]
index_standard = np.argsort(np.array(diff))[::-1]
pairs_sorted_standard = [pairs[i] for i in index_standard]

'''對'差'做分類,找出有幾種不同的差值,並存入val_diff中'''
res = np.array(diff)
val_diff = []
while res.size != 0:
    val_diff += [res[0]]
    res = np.delete(res,np.where(res == res[0])[0])
'''針對不同的差值由大到小排序,並賦予pairs新的順序'''
val_diff = np.sort(np.array(val_diff))[::-1] # 此時_val_diff變成array-->dim = (int,)
pairs_sorted = []
for val in val_diff:
    index = np.where(diff == val)[0] # index是array-->dim = (int64,)
    pairs_sorted += [pairs[i] for i in index]
    
'''bool mask 移除-->array'''
arr_mask = np.ones(len(pairs_sorted),dtype = bool)
for i in range(len(pairs_sorted)):
    if pairs_sorted[i][0] < 2 and pairs_sorted[i][1] > 5:
        arr_mask[i] = False
pairs_sorted_arr_cut = np.array(pairs_sorted)[arr_mask]

list_mask = [True for i in range(len(pairs_sorted))]
for i in range(len(pairs_sorted)):
    if pairs_sorted[i][0] < 2 and pairs_sorted[i][1] > 5:
        pairs_sorted[i] = False
[b for a, b in zip(list_mask, pairs_sorted) if a]
 # list indices must be integers or slices, not list
        
letter = 'aaabsaax'
length = [3,2]
p = []
p += [letter[0] * max(length)]