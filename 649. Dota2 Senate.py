# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:41:30 2021

@author: Brian
"""
'''
本題關鍵：在每一位有權利投票的人中，只要敵對陣營的人還在，一定要優先禁言在自己之後的敵方陣營人士，
          因為在字記後方的敵人有可能會在之後的投票中把自己的發言權禁止，如果自己後方沒有敵人的話，
          再考慮禁言自己之前的敵人，防止他在下一輪進言自己。總而言之，此種類型的題目的優先考慮都是
          讓自己盡可能的活到下一輪。
*** 撰寫程式時需要注意
(a) 如果刪除的人是自己之前的人，索引值(i)不需要位移，因為刪除的同時就是在變相位移一個位置
    如果刪除的人是自己之後的敵人，索引值(i)需要位移，因為索引值是由前往後數，刪除之後的人不影響自己的索引值
(b) 因為本題的字串長度一值在變，因此如果索引值大於或等於當前長度時，即進行下一輪投票，更新索引值(i)為0
'''
# senate = "DRRD"
senate = "DRRDRDRDRDDRDRDR"
i = 0
l = len(senate)
while True:
    if senate[i] == 'R':
        if (jb := senate.find('D',i)) == -1: # 第一個在自己之後的敵人位置
            if (jf := senate.find('D',0)) == -1: # 在自己之前的敵人位置
                print('Radiant')
                break
            else:
                senate = senate.replace(senate[jf],'',1) # i 不用位移，因為是刪除前面的人
        else:
            senate = senate[:i] + senate[i:].replace(senate[jb],'',1)
            i += 1 # i 要位移，因為是刪除後面的人
        l -= 1
        print(senate,'next start:',i)
    else:
        if (jb := senate.find('R',i)) == -1: 
            if (jf := senate.find('R',0)) == -1:
                print('Dire')
                break
            else:
                senate = senate.replace(senate[jf],'',1)
        else:
            senate = senate[:i] + senate[i:].replace(senate[jb],'',1)
            i += 1
        l -= 1
        print(senate,'next start:',i)
    if i >= l:
        i = 0


