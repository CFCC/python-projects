#!/usr/bin/python

for i in range(100):
    if i % 3 == 0:
        print str(i) + " is evenly divisible by three."
    elif i % 2 == 0:
        print str(i) + " is evenly divisible by two."
    else:
        print str(i) + " is not evenly divisible by two or three."


