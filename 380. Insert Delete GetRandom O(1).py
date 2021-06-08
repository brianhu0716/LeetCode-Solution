# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:56:33 2021

@author: Brian
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #import random
        self.set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        len_prev = len(self.set)
        self.set.add(val)
        return False if len_prev == len(self.set) else True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.set: return False
        self.set.remove(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(list(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()