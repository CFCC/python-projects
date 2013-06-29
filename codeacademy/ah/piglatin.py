# For exit() - AH
import sys

print "Welcome to the English to Pig Latin translator!"
# Get word from user
get_word = raw_input("Enter a word to be translated: ")
# If it is a valid word
if (not get_word == "") & get_word.isalpha():
    print "Translating " + get_word
# If it is not a valid word
else:
    print "Invalid input word"
    sys.exit(0)
# First letter of input word
first_letter = get_word[0]
vowels = "aeiou"
translated = ""
is_translated = False
# Check if first letter of word is a vowel
for i in range(4):
    # If it is a vowel, append "ay" and set is_translated to true
    if first_letter == vowels[i]:
        translated = get_word + "ay"
        is_translated = True
# If word has not already been translated (does not start with a vowel)
if is_translated == False:
    # Each letter of word starting at the second one
    for j in range(1, len(get_word)):
        translated += get_word[j]
    # Append first letter of word and "ay"
    translated += first_letter + "ay"
# Print final result
print "Translated word: " + translated
