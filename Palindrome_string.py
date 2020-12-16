"""
Palindrome String

Description
Write a program to check whether a string is a palindrome or not. 
Print 1 if the string is a palindrome and 0 otherwise.

Note: Please ensure that your program should not be case-sensitive. 
So, if the input is, say, “HAnnah”, then, its output should be 1.

Input:
A string

Output:
1 if the string is a palindrome, 0 otherwise

Sample input:
HAnnah

Sample output:
1

Sample input:
Rebecca

Sample output:
0
"""

input_string = 'HAnnah'

input_string = input_string.lower()
"""
palindrome = ''

for i in input_string:
	palindrome = palindrome + i

if palindrome == input_string:
	print(1)


else:
	print(0)
"""

option 2:

palindrome = input_string[::-1]

if palindrome == input_string:
	print(1)
else:
	print(0)