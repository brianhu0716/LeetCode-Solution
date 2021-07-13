# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:21:30 2021

@author: Brian Hu
"""

import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        
        # I am more of a list comprehensions guy, but if you prefer to
        # put more effort with the keyboard, here's an unrolled version.
        
        # self.weights = []
        # for rect in rects:
        #     x1, y1, x2, y2 = rect
        #     area = (x2-x1+1)*(y2-y1+1)
        #     self.weights.append(area)
        
        self.weights = [(x2-x1+1)*(y2-y1+1) for x1, y1, x2, y2 in rects]
        
            
        # library functions are always faster
        # it beats the runtime of using an extra variable 
        # to calculate sum_of_weights in the loop above
        # even if that means, we have to iterate once more.
        # Such is the world of python :D
        sum_of_weights = sum(self.weights)
        
        self.weights = [x/sum_of_weights for x in self.weights]
            

    def pick(self) -> List[int]:
        rect = random.choices(
            population=self.rects,
            weights=self.weights,
            k=1
        )[0]  # random.choices returns a list, we extract the first (and only) element.

        x1, y1, x2, y2 = rect  # tuple unpacking
        
        rnd_x = random.randint(x1, x2)
        rnd_y = random.randint(y1, y2)
        return [rnd_x, rnd_y]