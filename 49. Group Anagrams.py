class Solution:
    def groupAnagrams(self, strs):
        anagrams = []
        res = []
        remove = []
        while strs:
            # print('剩餘字串:',strs,'長度為:',len(strs))
            flag = strs[0]
            res += [flag]
            remove += [0]
            lf = len(flag)
            # print('當前旗標字串:',flag)
            for i in range(1,len(strs)):
                candidate = strs[i]
                lc = len(candidate)
                # print('當前判斷字串:',candidate)
                if lc != lf :
                    continue
                else:
                    for j in range(len(flag)):
                        candidate = candidate.replace(flag[j],'',1)
                        if len(candidate) == lc:
                            break
                        else:
                            lc -= 1
                        
                if lc == 0 :
                    remove += [i]
                    res += [strs[i]]
                    print(res)
                        
            anagrams += [res]
            res = []
            # print('移除位置:',remove)
            print('\n')
            
            strs = [strs[index] for index,value in enumerate(strs) if index not in remove]
            remove = []
        
        # print(anagrams)
        return anagrams

["","b"]
["eat","tea","tan","ate","nat","bat"]
strs = ["","b",""]
# strs = ["stop","pots","reed","","tops","deer","opts",""]

test = Solution()
test.groupAnagrams(strs)
