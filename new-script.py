#!/bin/python3

import sys #system function and parameters

from datetime import datetime
print(datetime.now())

#print(sys.version) - to print sys module version

from datetime import datetime as dt #import with alias named dt to shorten
print(dt.now())


my_name = "Health"
print(my_name[0]) #printout first letter
print(my_name[-1]) #printout last letter


sentence = "This is a sentence"
print(sentence[:4]) #will print "This"

print(sentence.split()) #breaks to individual words based on space delimeter

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) #joins words everytimne it sees space
print(sentence_join) 


quote = "He said, \"give me all your money\"" #backslash
quote1 = 'He said, "give me all your money"' #single quote
print(quote)
print(quote1)


too_much_space = "                hello       "
print(too_much_space.strip())

print("A" in "Apple") #means it is true bec A exists in Apple






