# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:54:03 2021

@author: -
"""
'''
該2D matrix 具有以下特色：每一行的由上到下以及每一列的由左到右的數字都是由小到大排序的
我們希望找出target是否在該2D矩陣中，思路如下:
(a) 我們直接檢視對角線的元素index = (1,1),(2,2)...(n,n)且n = min(行數,列數)以避免該矩陣為長方形
    只要目標比對角線的元素還要大，直接找下一個角線元素值比序，直到該對角線元素值大於等於target為止
(b) 若第一個大於target的對角線元素位置為(id,id)，則行、列依次由[id:n]進行搜索直到找到目標為止
(c) 若無法找到目標且2D matrix為方陣，則return False，否則index由n + 1開始繼續往長邊的邊界找，若還是沒有
    則return False
'''
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        l,w = len(matrix[0]),len(matrix)
        for id in range(l if l <= w else w): # id 代表對角線索引值(index of diagonal)，搜索時以短邊為界(包含等號)
            if matrix[id][id] >= target:
                while True:
                    if matrix[id][0] <= target: # 該列的第一個數字小於target(代表target可能在該列中)
                        for j in range(id + 1):
                            if matrix[id][j] == target:
                                return True
                            elif matrix[id][j] > target:
                                break
                    if matrix[0][id] <= target: # 該行的第一個數字小於target(代表target可能在該行中)
                        for i in range(id + 1):
                            if matrix[i][id] == target:
                                return True
                            elif matrix[i][id] > target:
                                break
                    if id + 1 < min(l,w) - 1:
                        id += 1
                    else :
                        break
        if l == w:
            return False
        else:
            if l - 1 > id:
                for j in range(id + 1,l):
                    if matrix[-1][j] >= target and matrix[0][j] <= target:
                        for i in range(w):
                            if matrix[i][j] == target:
                                return True
                            elif matrix[i][j] > target:
                                break
            elif w - 1 > id:
                for i in range(id + 1,w):
                    if matrix[i][-1] >= target and matrix[i][0] <= target:
                        for j in range(l):
                            if matrix[i][j] == target:
                                return True
                            elif matrix[i][j] > target:
                                break
        return False
matrix = [[5,6,10,14],[6,10,13,18],[10,13,18,19]]
target = 14
test = Solution()
print(test.searchMatrix(matrix, target))

'''
# binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            if len(arr)<1:
                return -1
            left, right = 0, len(arr)-1
            while left<=right:
                mid = (left+right) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        
        for row in matrix:
            if row[-1] < target:
                continue
            elif row[0]> target:
                return False
            else:
                result = binary_search(row, target)
                if result != -1:
                    return True
                
        return False
'''
'''
O(m + n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        i,j=0,m-1
        while i<n and j>=0:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                j-=1
            else:
                i+=1
        return False
'''