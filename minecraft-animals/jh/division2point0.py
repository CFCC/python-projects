#!/usr/bin/python

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print "FizzBuzz(" + str(i) + ") is a multiple of three and five."
    elif i % 3 == 0:
        print "Fizz(" + str(i) + ") is a multiple of three."
    elif i % 5 == 0:
        print "Buzz(" + str(i) + ") is a multiple of five."
    else:
        print str(i) + " is a multiple of neither three nor five."

