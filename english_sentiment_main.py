#!/usr/bin/env python
# -*- coding: utf-8 -*-

from english_sentiment_module import func,func2

import io
fo=io.open('engReviews.txt','r',encoding='utf-8')
text=fo.read()
fo.close()
seperator='========================='
word=text.split()
wlist=[]
#print(word)
#len(word)
count=0

for wd in word:
    if wd == seperator:
        count+=1
        i=0
        p=[]
        print('User:')
        print(count)
        while i<len(wlist):
            p.append(wlist.pop())

        func(p)
        func2(p)
        #print(p)
        
    else:
        wlist.append(wd)



