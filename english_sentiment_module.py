#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func(rev):
    
    def readfile(fileName):
        
        import io
        f=io.open(fileName,'r',encoding='utf-8')
        ret = []
        
        for line in f:
            ret += line.split()
        return ret

    goodWords=readfile('goodwords.txt')
    badWords=readfile('badwords.txt')

    global goodCount
    global badCount
    
    goodCount=0
    badCount=0

    for word in rev:    

        if word in goodWords:
            goodCount+=1
        
        if word in badWords:
            badCount+=1


    if goodCount>badCount:
        print("Positive Sentiment")
        import pyttsx
        engine = pyttsx.init()
        engine.say('Positive sentiment.')
        engine.runAndWait()

    elif goodCount<badCount:
        print("Negative Sentiment")
        import pyttsx
        engine = pyttsx.init()
        engine.say('Negative sentiment.')
        engine.runAndWait()


    elif goodCount==badCount and goodCount!=0 and badCount!=0:
        print("Neutral Sentiment")
        import pyttsx
        engine = pyttsx.init()
        engine.say('Neutral sentiment.')
        engine.runAndWait()


    elif goodCount==0 and badCount==0:    
        print("Sorry can't generate the Sentiment")
        import pyttsx
        engine = pyttsx.init()
        engine.say('Sorry cannot generate the Sentiment.')
        engine.runAndWait()
        return
    print("Number of Good Count(s): ",goodCount)
    print("Number of Bad Count(s): ",badCount)

   


    input("")

def func2(li):
    li.reverse()
    stri=' '
    leng=len(li)
    for i in range(0,leng):
        stri+=li[i]
        stri+=' '
    print(stri)
    fi=open('reviewResult.txt','a',encoding='utf-8')
    fi.write('\n\n'+stri+'\t')

    if goodCount>badCount:
        fi.write("Positive Sentiment")
    elif goodCount<badCount:
        fi.write("Negative Sentiment")
    elif goodCount==badCount  and goodCount!=0 and badCount!=0:
        fi.write("Neutral Sentiment")
    elif goodCount==0 and badCount==0:
        fi.write("Sorry can't generate the Sentiment\n")
        fi.write('-------------------------------------------------------------------')
        fi.close()
        
        return
        
    fi.write('\n'+'Weightage Ratio:')
    fi.write('\n'+"Good : Bad = ")
    fi.write(str(goodCount)+':'+str(badCount))
    fi.write('\n\n')
    fi.write('-------------------------------------------------------------------')
    fi.close()
    


