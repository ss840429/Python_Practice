#!/usr/bin/env python

import os

cmd = 'ls /home'
dirList = os.popen(cmd).readlines()
dirSize = []

for l in dirList:
    quest = 'du -s /home/'+l.strip()
    size = os.popen(quest).readlines()
    dirSize.append( size[0].split('\t'))

dirSize.sort( key=lambda x:x[0], reverse=True)
for l in dirSize:
	unit = " KB"
	print("Usage : {0:10} KB\tDir : {1:10}".format(l[0], l[1].strip()))
