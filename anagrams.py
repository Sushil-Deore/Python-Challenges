"""
Anagrams

Description
Two strings are anagrams of each other if you can rearrange 
the characters of one string to make the other string.
Given two strings, can you find if they are anagrams or no?

Input:
Two lines of input, each line will contain a string without space.

Output:
True or False based on whether the strings are anagrams or not.

Sample input:
thing
night

Sample output:
True

Sample input:
upgrad
found

Sample output:
False

Note: the code will be case-Sensitive
Hint: if the length of the strings doesn't match,
the strings are obviously not anagrams.
"""

string_1 = 'thing'
string_2 = 'night'

def anagram(string_1,string_2):
	data = []
	for i in string_1:
		if i in string_2:
			data.append(i)

	if len(data) == len(string_1):
		return True
	else:
		return False

print(anagram(string_1, string_2))