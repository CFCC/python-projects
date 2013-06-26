#!/usr/bin/python

for i in range(100):
	if i % 3 == 0:
		print str(i) + " is evenly divisable by 3"
	elif i % 2 == 0:
		print str(i) + " is evenly divisable by 2"
	else:
		print str(i) + " is not evenly divisible by 2 or 3"
