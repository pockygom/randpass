#!/usr/bin/env python2.7
# Mark Saad 
# mark.saad@ymail.com
# 7July2016
# A Silly random password generator 

import linecache
from random import randint

rnum1 = randint(1,1000)
word1 = linecache.getline('common-words.txt', rnum1)
rnum2 = randint(1,1000)
word2 = linecache.getline('common-words.txt', rnum2)
rnum3 = randint(1,1000)
word3 = linecache.getline('common-words.txt', rnum3)

line = word1.rstrip()+word2.rstrip().title()+word3.rstrip().title()+str(randint(1000,9999)).rstrip()

print "Your random password is:", line

