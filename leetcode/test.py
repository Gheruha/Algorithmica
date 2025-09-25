# Palindrome/ Anagram

# Palindrome Solution
word = "Madam"
if word[::-1].lower() == word.lower():
    print("Palindrome")
else:
    print("Not Palindrome")

""" Anagram Solution
 Given two strings s1 & s2, implement a solution to see if they are anagram or not

 2 words are anagrams when:
 - they have exactly the same characters
 - they are not the same
 - the order of the characters does not matter
"""

s1 = "night"
s2 = "thing"

if len(s1) == len(s2) and sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
