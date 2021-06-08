# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:43:17 2021

@author: Brian
"""
'''
紀錄每一次的更動範圍，當某位置被呼叫時，只要由後往前看找到最近一次的更動範圍有包含被呼叫的位置，回傳該次更動值即可
'''
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.operation = list()

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.operation.append([row1,row2,col1,col2,newValue])

    def getValue(self, row: int, col: int) -> int:
        for ope in self.operation[::-1]:
            if max(ope[1],ope[0]) >= row >= min(ope[1],ope[0]) and max(ope[2],ope[3]) >= col >= min(ope[2],ope[3]):
                return ope[4]

        return self.rectangle[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
    