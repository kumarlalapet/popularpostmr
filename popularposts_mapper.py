#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    
    idfield,title,tag,authid,body,nodetype,pid,apid,addedat,score,sstr,leid,labid,laat,arid,extra,exrid,excnt,mkd = line
    
    if idfield == "id":
        continue
    
    if nodetype == "comment":
        result = []
        result.append(pid)
        result.append("C")
        result.append(1)
        writer.writerow(result)
    elif nodetype == "answer":
        result = []
        result.append(pid)
        result.append("A")
        result.append(1)
        writer.writerow(result)

