# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:42:31 2021

@author: Brian
"""
'''
import numpy as np
x = np.array([1,2,2,1,6,7,7])
sort_x = list()
count = 0
while len(x) != 0:
    index = np.where(x == min(x))[0]
    sort_x += [min(x)]*len(index)
    x = np.delete(x,index)
    count += 1
    if count == 10:
        break
'''

'''
boolin mask-->解決一個array中同時要拿掉多個值時用'''
import numpy as np
x = np.array([1,2,1,3,4,1]);print('原始陣列:',x)
index = np.where(x == min(x))[0] # 等同於index = np.where(x == min(x));index = index[0]
mask = np.ones(len(x),dtype = bool)
mask[index] = False
x = x[mask];print('拿掉最小值1後的陣列:',x)

'''np.delete及實現排序的做法'''
nums = np.array([1,2,-1,23,4,1]);print('原始陣列:',nums)
nums_sorted = list()
while nums.size != 0:
    index = np.where(nums == min(nums))[0]
    nums_sorted += [min(nums)]*len(index) # z = [2]*4,z=[2,2,2,2]
    nums = np.delete(nums,index)
print('排序後的陣列:',nums_sorted)