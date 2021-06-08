# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:13:00 2021

@author: brian.hu
"""

class Solution:
    def numTeams(self, arr: List[int]) -> int:
		# cache to store indices which have a value greater than current index
        memoGreater = {}
        
		# cache to store indices which have a value lesser than current index
        memoLesser = {}
        length = len(arr)
        
        for i in range(length):
            memoGreater[i] = []
            memoLesser[i] = []
            for j in range(i+1, length):
                if arr[j] > arr[i]:
                    memoGreater[i].append(j)
                elif arr[j] < arr[i]:
                    memoLesser[i].append(j)
        
        numTeams = 0
		# add the teams using the conditions specified
        for i in range(length):
            for index in memoGreater[i]:
                numTeams += len(memoGreater[index])
            for index in memoLesser[i]:
                numTeams += len(memoLesser[index])
        
        return numTeams