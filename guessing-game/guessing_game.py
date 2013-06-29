# Simple number guessing game - AH

import random

correct_answer = random.randint(1, 100)
tries = 0
for i in range(10):
    user_answer = raw_input("Enter a number: ")
    if not user_answer.isdigit():
        print "Given answer is not a number"
        break
    user_answer = int(user_answer)
    if not 1 <= user_answer <= 100:
        print "Given answer is out of acceptable range"
        break
    elif user_answer == correct_answer:
        print "Correct"
        break
    elif user_answer < correct_answer:
        print "Too low"
    elif user_answer > correct_answer:
        print "Too high"
    else:
        print "Something went wrong"
    tries += 1
    if tries == 10:
        print "Out of tries"
        break
