
import os
import sys
import itertools as its


words = ['123', 'qwe', 'zxc', '0-=', '[]\\', ',./']
r1 = its.product(words, repeat=4)
dic = open("pass1.txt", "a")
for i in r1:
    i = list(i)
    temp = ""
    for k in i:
        temp = temp+k
    dic.write(temp+'\n')
r2 = its.product(words, repeat=5)
for i in r2:
    i = list(i)
    temp = ""
    for k in i:
        temp = temp+k
    dic.write(temp+'\n')
r3 = its.product(words, repeat=6)
for i in r3:
    i = list(i)
    temp = ""
    for k in i:
        temp = temp+k
    dic.write(temp+'\n')