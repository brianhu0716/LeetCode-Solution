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

import json
import string
from random import randint
a = [[None for _ in range(500)] for _ in range(500)]
for i in range(500):
    for j in range(500):
        idx = randint(0, 25)
        a[i][j] = string.ascii_lowercase[idx]
print(json.dumps(a))
