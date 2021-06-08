# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:36:56 2021

@author: Brian
"""

'''
對長Url進行編碼，我們的做法為取長Url的前面第一個"/"之前的字元，結合後面到第一個"/"後的字元，如
長Url : "https://leetcode.com/problems/design-tinyurl"
第一階段編碼後："https://design-tinyurl" + "//" -- > "https://design-tinyurl//"
接著第二階段編碼為在第一階段編碼後加上5個隨機生成的英文字母或數字，完成後即可把該密碼存入字典中，方便讀取之後對應的原始網頁
*** 注意random以及string函數的用法，產生隨機數字與法；random.choice(string.digits)，產生隨字母：random.choice(string.ascii_letters)
'''
import random
import string
class Codec:
    def __init__(self):
        self.d = dict()
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encode = longUrl[:longUrl.find("/") + 1] + longUrl[longUrl.rfind("/"):] + "//"
        for i in range(5):
            flag = random.randint(0,2)
            if flag == 1: encode += random.choice(string.ascii_letters) # 隨機選到1-->產生隨機字母
            else : encode += random.choice(string.digits) # 隨機選到0-->產生隨機數字
        self.d[encode] = longUrl
        #print(encode)
        return encode
            
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        for code in self.d.keys():
            if code == shortUrl : return self.d[code]