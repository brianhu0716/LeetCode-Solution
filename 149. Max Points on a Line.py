# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:27:35 2021

@author: Brian
"""
'''
本題分三種情況討論:
(a) 若分母相同，分子不同時: 為鉛直線，只需要判斷x = ? 即可，因此key只需要一個x值
(b) 若分母不同，分子相同時: 為水平線，只需要判斷y = ? 即可，因此key只需要一個y值
(c) 若分子分母都不同，此時我們需要考慮斜率以及偏移量兩項參數，因此key為(slope,shift)
***為了避免重複加入座標值(ex:[[1,1],[2,2],[3,3]])的情況，若key值已經存在相對應的字典中
    我們一律只新增後一個座標(因城市演算法的緣故，前一個座標一定已被儲存)
***如果points只有一個座標，直接給1
'''
class Solution():
    def maxPoints(self,points):
        bigD = {}
        bigD['o'] , bigD['h'] , bigD['v'] = {}, {}, {} # other,horizental,vertical
        for i in range(len(points)):
            for j in range(i + 1,len(points)):
                if points[i][0] == points[j][0] and points[i][1] != points[j][1]:
                    r = points[i][0]
                    if r not in bigD['v'].keys():
                        bigD['v'][r] = [points[i],points[j]]
                    else: 
                        if points[j] not in bigD['v'][r]:
                            bigD['v'][r] += [points[j]]
                            # print(points[i],points[j])
                elif points[i][0] != points[j][0] and points[i][1] == points[j][1]:
                    r = points[i][1]
                    if r not in bigD['h'].keys():
                        bigD['h'][r] = [points[i],points[j]]
                    else:
                        if points[j] not in bigD['h'][r]:
                            bigD['h'][r] += [points[j]]
                            # print(points[i],points[j])
                else :
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    shift = points[i][1] - slope * points[i][0] # 避免斜率相同但位移不同的情況
                    if (slope,shift) not in bigD['o'].keys():
                        bigD['o'][(slope,shift)] = [points[i],points[j]]
                    else:
                        if points[j] not in bigD['o'][(slope,shift)]:
                            bigD['o'][(slope,shift)] += [points[j]]
                            # print(points[i],points[j])
        N = 1 # 如果points只有一個座標的話，直接給1
        for key in bigD.keys():
            if not bigD[key]:
                continue
            else:
                N = max(max([len(bigD[key][l]) for l in bigD[key].keys()]),N)
        print('共線最多的點數為:',N)

test = Solution()
points = [[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],
          [[1,1],[2,2],[3,3]],
          [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]],
          [[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]],
          [[0,0],[2,2],[-1,-1]]]

for i in points:
    test.maxPoints(i)