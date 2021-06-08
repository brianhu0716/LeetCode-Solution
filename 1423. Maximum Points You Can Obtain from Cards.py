# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:11:59 2021

@author: Brian
"""
'''
每次動作可以從頭或偉拿走一個數字，目的是在拿k次時使被拿走的數字總和會最大。本題的提意可以轉換為找出一個長度為l - k 的連續窗口，
使連續窗口內部的和為最小，最後再把原始序列加總後減去該窗口的最小和，即可最大化由頭或尾連續拿k次的數字和
(a) 我們先計算第0到第l - k - 1的和作為起始窗口，並把該窗口的和初始化為最小值
(b) 接著每次向右滑動一個位置，同時更新目前窗口的和(更新方法為減去前一個連續窗口的第一個值並加上當前窗口的最後一個值即可，不需要重
    復計算)；只要當前的窗口和比最小窗口和還小，即更新最小窗口和，等到左指標滑到index = k時，窗口尾部的index = l - k + k - 1
    (剛好是最後一個位置)，結束程式。
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        ref = sum(cardPoints[:l - k])
        min_sum = ref
        for lp in range(1,k + 1):
            n_before_first = cardPoints[lp - 1]
            n_last = cardPoints[l - k + lp - 1]
            sum_now = ref - n_before_first + n_last
            if sum_now < min_sum: min_sum = sum_now
            ref = sum_now
        return sum(cardPoints) - min_sum