# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:57:14 2021

@author: Brian Hu
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand)) % groupSize != 0 : return False  # special case
        hand.sort()
        dq = deque([])
        for num in hand:
            if not dq:
                dq.append([num])
                if len(dq[0]) == groupSize: # if the sequence size == groupSize, eliminate it
                    dq.popleft()
            else:
                for j in range(len(dq)):
                    seq = dq[j]
                    if num - seq[-1] > 1:
                        return False
					 # any sequence left in dq at least needs one number to make it size ==  groupSize. 
					 # If current number greater than the maxima of sequence, it means a gap appears 
					 # and imply the sequence can't become a consecutive sequence with size == groupSize
                    elif num - seq[-1] == 1:
                        if len(seq) == groupSize - 1: # sequence size == groupSize, eliminate it ! 
                            dq.popleft()
                        else:
                            seq.append(num) # else update the sequence
                        break
                    else:
                        if j == len(dq) - 1: # if max number in last sequence is equal to current number, we create another new sequence to put it in
                            dq.append([num])

        if dq:  # if dq still remains sequence, return False
            return False
        return True