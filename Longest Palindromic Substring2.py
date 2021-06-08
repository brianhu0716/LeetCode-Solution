
import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.palindrome = []
        for i in range(len(self.s)):            
            self.index = np.where(np.array([item for item in self.s]) == self.s[i])[0]           
            if self.index.size > 1:
                self.findLetterNum()
                for pair in self.pairs_sorted:  # self.pairs_sort = [[],[],...]
                    self.furtherSearch(start = pair[1],end = pair[0])
                    if self.palindrome:
                        return self.palindrome[0]
        if not self.palindrome:
            self.palindrome += self.s[0] 
            return self.palindrome[0]
        else:
            length = np.array([len(self.palindrome[i]) for i in range(len(self.palindrome))])
            return self.palindrome[np.where(length == np.max(length))[0]]
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
            self.palindrome += [self.s[end:start + 1]] 
    def findLetterNum(self):
        res = np.array([self.s[i] for i in range(len(self.s))])
        letters = []
        while res.size != 0:
            letters += [res[0]]
            res = np.delete(res,np.where(res == res[0])[0])
        self.findPairs(letters)
    def findPairs(self,letters):
        self.pairs = []
        self.diff = []
        res = np.array([self.s[i] for i in range(len(self.s))])
        for letter in letters:
            self.index = np.where(res == letter)[0] 
            for i in range(len(self.index)):
                for j in range(i + 1,len(self.index)):
                    self.pairs += [(self.index[i],self.index[j])]
                    self.diff += [self.index[j] - self.index[i]]
        self.generatePairs()
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

        
    # def cutPairs(self,wrongflag):
    #     mask = np.ones(len(self.pairs_sorted),dtype = 'bool')
    #     cut_ind = []
    #     for i in range(len(self.pairs_sorted)):
    #         if self.pairs_sorted[i][0] < wrongflag[0][0] and self.pairs_sorted[i][1] > wrongflag[0][1]:
    #             cut_ind += [cut_ind]
    #     mask[cut_ind] = False
    #     self.pairs_sorted = self.pairs_sorted[mask]

s = ["babad", # bab
      "cbbd", # bb
      "a", # a
      "ac", # a
      "aacabdkacaa", # aca 
      "abbcccbbbcaaccbababcbcabca",
      "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"] # aca       


# s = ["ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw"]
test = Solution()
for string in s:
    test.longestPalindrome(string)
    print(test.palindrome)   
    # print(test.pairs_sorted)

        
            
                