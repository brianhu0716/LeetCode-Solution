# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 08:26:49 2021

@author: Brian Hu
"""
from random import randint

n = 3 * 10 ** 4
data = []
for i in range(n):
    flag = randint(0, 1)
    if flag == 1:
        