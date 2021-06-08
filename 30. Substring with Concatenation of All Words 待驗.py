# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:28:58 2021

@author: Brian
"""

class Solution:
    def findSubstring(self, s, words):
        ls = len(s)
        shift = len(words[0])
        unused = [word for word in words]
        used = []
        start = -1
        flag = []
        i = 0
        while i + shift - 1 <= ls - 1:
            print('現在的索引值:',i)
            ss = s[i:i+shift]
            if ss in unused:
                if start == -1:
                    start = i     
                unused.remove(ss)
                used += [ss]
                i += shift
                print('unused1',unused)
                print('used1',used)
            else:
                if ss not in used:
                    i += shift 
                    start = i
                    unused = [word for word in words]
                    used = []
                    print('unused2',unused)
                    print('used2',used)
                else:
                    position = used.index(ss)
                    unused += used[:position]
                    used = used[position + 1:] + [ss]
                    start += (position + 1) * shift
                    i = start
                    print('unused3',unused)
                    print('used3',used)
                    
            
            
            if not unused :
                flag += [start]
                start = i + shift
                c = 0
                while start + shift - 1 <= ls - 1:
                    if s[start:start + shift] == used[0]:
                        used += [used[0]]
                        used.remove(used[0])
                        flag += [start]
                        start += shift
                        c += 1
                    else:
                        i = flag[-1] + c * shift
                        start = i
                        used = []
                        break
        print(flag)
                    # for j in range(i+shift,ls,shift):
                    #     if s[j:j+shift] in unused:
                    #         ss = s[j:j+shift]
                    #         unused.remove(ss)
                    #         used += [ss]
                    #     else:
                    #         if s[j:j+shift] in used:
                    #             position = used.index(s[j:j+shift])
                    #             unused += used[:position]
                    #             used += used[position+1:] + [s[j:j+shift]]
                    #             i = j + shift
                    #             flag = position + shift
                    #             break
                    #         else:
                    #             i = j + shift
                    #             flag = i
                    #             break
                
            
    
test = Solution()
case = [("barfoothefoobarman",['foo','bar']), # [0,9]
        ("wordgoodgoodgoodbestword",["word","good","best","word"]), # []
        ("barfoofoobarthefoobarman",["bar","foo","the"])] # [6,9,12]
# case = [("aaa",["a","a"])]
case = [("barfoofoobarthefoobarman",["bar","foo","the"])]
for i in range(len(case)):
    test.findSubstring(case[i][0],case[i][1])
    # ans += [test.start]
# print(ans)