#!/usr/bin/env python

import os

cmd = "w -sh | awk '{print $2, $3}' "
userList = os.popen(cmd).readlines()


for l in userList:
	time = l.split(' ')
	idle = time[1].strip()
	if idle.endswith('days') or (idle.endswith('m') and (int(time[1].strip()[-3:-1]) >= 30 or int(time[1].strip()[0:1]) >= 1)):
		print('pkill -kill -t '+time[0]) 
# 		os.system('pkill -kill -t '+time[0])		# Prevent execute

		
