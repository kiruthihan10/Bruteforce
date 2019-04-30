# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 22:24:03 2018

@author: kirut
"""

def next(word):
    if len(word) !=1:
        if word.count('~') == len(word):
            new_word = "!"
            for letter in word:
                new_word += '!'
            word = new_word
        else:
            if len(next(word[1:])) >= len(word):
                new_word = chr(ord(word[0])+1)+next(word[1:])[1:]
                True
            else:
                new_word = word[0]+next(word[1:])
            word = new_word
        return word
    else:
        if word != '~':
            word= chr(ord(word)+1)
        else:
            word = "!!"
        return word

def main(n):
    words = []
    word="!"
    while len(word)<n:
        word=next(word)
        words.append(word)
        print (word)
    print ("end")
    print (len(list(words)) == len(words))
import time
start_time = time.time()        
main(3)
print ("---%s seconds -------"%(time.time()-start_time))
