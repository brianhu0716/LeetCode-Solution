#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 05:43:30 2021

@author: brian
"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start = 0
        t_wait = 0
        for idx,(t_in,t_prep) in enumerate(customers) :
            if (idx == 0) or (idx > 0 and t_in >= start) : # customer don't need to wait
                t_wait += t_prep
                start = t_in + t_prep
            else : # wait time = start time - time when the customer get in the shop + time to prepare the meal
                t_wait += (start - t_in) + t_prep
                start += t_prep
        return t_wait / (idx + 1)