# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 00:57:31 2021

@author: Brian
"""

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        def findNext(start, clips, flag, l, time):
            for k in range(start, l):
                if clips[k][0] > flag: # stop greedy procedure
                    return k
                if clips[k][0] <= time <= clips[k][1]:
                    return k + 1
            return l
        clips.sort()
        if clips[0][0] > 0: # no where to begin
            return -1
        ans, l = 1, len(clips) 
        for i in range(l):
            if clips[i][0] > 0: # stop greedy procedure
                break
            if clips[i][0] <= time <= clips[i][1]: # find answer
                return ans

        j = clips[i - 1][1]
        start = i
        while start < l:
            next = findNext(start, clips, j, l, time) # begin index of next round
            if next == start: # can't push further and still not reach "time"
                return -1
            if clips[next - 1][0] <= time <= clips[next - 1][1]:
                return ans + 1 if (j < time) else ans # if j < time, we need to cut another clip to fill the last part of video
            elif clips[next - 1][0] <= j < clips[next - 1][1]:
                j = clips[next - 1][1] # update the maxima cover upper bound, so that we can minimize the number of clips
            else: # gap, can't push further and still not find answer
                return -1
            ans += 1 
            start = next
        return -1 # we review all clips but still can't make video interval from [0,time] happen