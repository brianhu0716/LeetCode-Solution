import numpy as np
# string = ['aab',
#      'baa',
#      'abaaa',
#      ]
# string = 'abaaacaaaa'
# string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# string = 'adam'
string = 'caba'
# string = 'bb'
letter = string[1]
p = []
palindrome = ''
#for s in string:
s = np.array([string[i] for i in range(len(string))])
index = np.where(s != letter)[0]
if index[0] != 0:
    p += [s[:index[0]]]
for i in range(len(index)-1):
    p += [s[index[i] + 1:index[i+1]]]
if index[-1] != len(s) - 1:
    p += [s[index[-1] + 1:]]
if len(p) == 1:
    for i in range(len(p[0])):
        palindrome += p[0][i]
else:
    flag = len(p) - 1 # flag是還沒有插入回文格式的長度       
    shift = 2
    i = 0 # 計算內插回文格式的位置-->0,2,4,...
    if index[0] == 0:
        k = 1 # 計算即將插入回文的單一數字位置
    else:
        k = 0
    while True:
        min_repeat = min(len(p[i]),len(p[i+1]))
        res = p[i+1:]
        p[i+1] = np.array([letter for i in range(min_repeat)] + [s[index[k]]] + [letter for i in range(min_repeat)])
        # p[i+2:] = res
        p += res
        i += shift
        k += 1
        if k == flag:
            break
    
    length = [len(p[i]) for i in range(len(p))]                
    imax_len = length.index(max(length))
    for i in range(length[imax_len]):
        palindrome += p[imax_len][i]         
print(palindrome)