# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:45:10 2021

@author: Brian
"""
'''
把字串中出現於d的特殊字元置換掉即可
'''
text = "and I quote: &quot;...&quot;"
i = 0
d = {'&quot;' : '\"',
    '&apos;' : "'",
    '&amp;' : '&',
    '&gt;' : '>',
    '&lt;' : '<',
    '&frasl;' : '/'}
while i < len(text):
    if text[i] == '&':
        for j in range(i + 1,len(text),1):
            if text[j] == ';':
                break
        if text[i : j + 1] in d.keys():
            text = text.replace(text[i : j + 1],d[text[i : j + 1]],1)
            i += 1
            print('1',text,i)
        else:
            i = j + 1
    else:
        i += 1
# text = ["&amp; is an HTML entity but &ambassador; is not."]
