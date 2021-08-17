# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:59:45 2021

@author: Brian Hu
"""
# import swagger_py_codegen
# from random import randint
# z = []
# for i in range(10 ** 5):
#     z.append(randint(-2 ** 31, 2 ** 31 - 1))

# import json
# import string
# from random import randint
# a = [[None for _ in range(500)] for _ in range(500)]
# for i in range(500):
#     for j in range(500):
#         idx = randint(0, 25)
#         a[i][j] = string.ascii_lowercase[idx]
# print(json.dumps(a))

"""
import random
n = 10 ** 4
vrange = [-10 ** 4, 10 ** 4]
nums = list()
queries = list()
for _ in range(n):
    nums.append(random.randint(vrange[0], vrange[1]))
    queries.append([random.randint(vrange[0], vrange[1]), random.randint(0, 9999)])
print(nums)
print(queries)
"""


import random
arr = []
for i in range(10 ** 5):
    arr.append(random.randint(1, 10 ** 4))
print(arr)
print(sum(arr))


"""
import random
for _ in range(10):
    arr = random.sample([i for i in range(0, 10)], k=10)
    print(arr)
"""
"""
import torch
for i in list(torch.randn(10)):
    print(i)
"""

"""
import random
n = 2 * 10 ** 4
nums = [None for _ in range(n)]
starts = random.sample([i for i in range(-10 ** 6, 10 ** 6 + 1)], k=n)
for idx, start in enumerate(starts):
    nums[idx] = [start, random.randint(start, 10 ** 6)]
print(nums)
"""