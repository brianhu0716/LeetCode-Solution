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

import numpy as np
n = np.arange(-30, 81, 1)

mask = np.where((-10 <= n) & (n <= 20) | (50 <= n) & (n >= 80), 1, 0)

print(mask)

