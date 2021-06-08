
import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.palindrome = ''
        
        self.findLetterNum()
        
        self.primaryJudge()
        if self.palindrome:
            return self.palindrome
        else:
            self.findPairs()
        self.generatePairs()
        
        for pair in self.pairs_sorted:  # self.pairs_sort = [[],[],...]
            self.furtherSearch(start = pair[1],end = pair[0])
            if self.palindrome:
                return self.palindrome
            
        # if not self.palindrome:
        #     self.palindrome += [self.s[0]]
        #     return self.palindrome[0]
            
        # else:
        #     length = np.array([len(self.palindrome[i]) for i in range(len(self.palindrome))])
        #     return self.palindrome[np.where(length == np.max(length))[0]]
    def furtherSearch(self,start,end):
        interval = int(np.floor((start - end) / 2))
        flag = True
        for shift in range(1,interval + 1):
            if self.s[start - shift] != self.s[end + shift]:
                # wrongflag = [(end + shift,start - shift)] #
                # self.cutPairs(wrongflag) #
                flag = False
                break
        if flag == True:
            self.palindrome = self.s[end:start + 1] 
    def findLetterNum(self):
        res = np.array([self.s[i] for i in range(len(self.s))])
        
        self.letters = []
        while res.size != 0:
            i = np.where(res == res[0])[0]
            if len(i) == 1:
                res = np.delete(res,i)
            else:
                self.letters += [res[0]]
                res = np.delete(res,i)
    def primaryJudge(self):
        length = []            
        res = np.array([self.s[i] for i in range(len(self.s))])
        if len(self.letters) == 0: # 'abnm..'(所有字母皆不相同),'a'(只有一個字母),''(沒有字母)
            self.palindrome = self.s[0]
        elif len(self.letters) == 1: 
            index = np.where(res != self.letters[0])[0]
            if index.size == 0: # 'aaaaaa...'(只有一字母且重複多次)
                self.palindrome = self.s[0:]
            else: # 'aaaaaaaceaaaw'(有一字母且重複多次且其餘只出現一次)
                s = np.array([self.s[i] for i in range(len(self.s))])
                self.p = []
                index = np.where(s != self.letters[0])[0]
                if index[0] != 0:
                    self.p += [s[:index[0]]]
                for i in range(len(index)-1):
                    self.p += [s[index[i] + 1:index[i+1]]]
                if index[-1] != len(s) - 1:
                    self.p += [s[index[-1] + 1:]]

                if index[0] == 0 and index[-1] != len(self.s) - 1: # 'baa...aacaa...' ,'ba....a'
                    if len(self.p) == 1:
                        self.palindrome = self.s[1:]
                    else:
                        flag = 1  # flag是要插入回文格式的單字的數量
                        k = 1 # 計算即將插入回文的單一數字位置
                elif index[0] != 0 and index[-1] == len(self.s) - 1: # 'aa...b...aac','a...ac'
                    if len(self.p) == 1:
                        self.palindrome = self.s[:-1]
                    else:
                        flag = 1
                        k = 0
                elif index[0] != 0 and index[-1] != len(self.s) - 1: # 'aa...b...c...aa'
                    flag = len(self.p) - 1
                    k = 0
                else:
                    if len(self.p) == 1: # 'ba...ac'
                        self.palindrome = self.s[1:-1]
                    else: # ba...va...c
                        flag = len(self.p) - 1
                        k = 1
                if self.palindrome:
                    return self.palindrome 
                
                shift = 2
                i = 0 # 計算內插回文格式的位置-->0,2,4,...
                while True:
                    min_repeat = min(len(self.p[i]),len(self.p[i+1]))
                    res1 = self.p[i+1:]
                    self.p[i+1] = np.array([self.letters[0] for i in range(min_repeat)] + [s[index[k]]] + [self.letters[0] for i in range(min_repeat)])
                    # p[i+2:] = res
                    self.p += res1
                    i += shift
                    k += 1
                    if k >= flag:
                        break

                length = [len(self.p[i]) for i in range(len(self.p))]                
                imax_len = length.index(max(length))
                for i in range(length[imax_len]):
                    self.palindrome += self.p[imax_len][i]  
        else:
            self.findPairs()

    def findPairs(self):
        self.pairs = []
        self.diff = []
        res = np.array([self.s[i] for i in range(len(self.s))])
        for letter in self.letters:
            self.index = np.where(res == letter)[0] 
            for i in range(len(self.index)):
                for j in range(i + 1,len(self.index)):
                    self.pairs += [(self.index[i],self.index[j])]
                    self.diff += [self.index[j] - self.index[i]]
        
    def generatePairs(self):
        # self.index_sorted = np.argsort(np.array(self.diff))[::-1] # [::-1]代表反向排序(大-->小)
        # self.pairs_sorted = [self.pairs[i] for i in self.index_sorted] 
        '''對'差'做分類,找出有幾種不同的差值,並存入val_diff中'''
        res = np.array(self.diff)
        val_diff = []
        while res.size != 0:    
            val_diff += [res[0]] # val_diff是list
            res = np.delete(res,np.where(res == res[0])[0])
        '''針對不同的差值由大到小排序,並賦予pairs新的順序'''
        val_diff = np.sort(np.array(val_diff))[::-1] # 此時_val_diff變成array-->dim = (int,)
        self.pairs_sorted = []
        for val in val_diff:
            index = np.where(self.diff == val)[0] # index是array-->dim = (int64,)
            self.pairs_sorted += [self.pairs[i] for i in index]


s = ["babad", # bab
      "cbbd", # bb
      "a", # a
      "ac", # a
      "aacabdkacaa", # aca 
      "abbcccbbbcaaccbababcbcabca",
      'abb',
      'aba',
      "ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw",
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      'caba',
      "abcbe",
      "eabcb"] # aca       
# s = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
# s = ['babad']
# s = ["ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw"]
test = Solution()
for string in s:
    test.longestPalindrome(string)
    print(test.palindrome)   
    # print(test.pairs_sorted)

        
            
                
            
                