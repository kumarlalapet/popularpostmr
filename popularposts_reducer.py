#!/usr/bin/python

import sys
import csv

answercount = 0
commentcount = 0
oldKey = None

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    data_mapped = line

    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        print oldKey , "\t" , commentcount , "\t" , answercount
        oldKey = thisKey
        answercount = 0
        commentcount = 0
    
    if data_mapped[1] == "C":
        commentcount = commentcount + 1
    elif data_mapped[1] == "A":
        answercount = answercount + 1

    oldKey = thisKey

if oldKey != None:
    print oldKey , "\t" , commentcount , "\t" , answercount
