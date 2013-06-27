#!/usr/bin/python

for i in range(100):
    if i % 2 == 0 and i % 3 == 0:
        print str(i) + " is evenly divisible by two and three."
    elif i % 2 == 0:
        print str(i) + " is evenly divisible by two."
    elif i % 3 == 0:
        print str(i) + " is evenly divisible by three."
    else:
        print str(i) + " is not evenly divisible by two or three."

