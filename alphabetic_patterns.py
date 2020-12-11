"""
Alphabetic patterns
Description
Given a positive integer 'n' less than or equal to 26, 
you are required to print the below pattern 
 
Sample Input: 5 
 
Sample Output : 
--------e-------- 
------e-d-e------ 
----e-d-c-d-e---- 
--e-d-c-b-c-d-e-- 
e-d-c-b-a-b-c-d-e 
--e-d-c-b-c-d-e-- 
----e-d-c-d-e---- 
------e-d-e------ s
--------e-------- 
"""

import random

n = random.choice([1,2,3,4,5,6,7,8,9])

def alphabetic_pattern(n):
	for i in range(1, n+1): # i = 1,2,3,4,5
		#first print --
		for s in range(n-i):
			print("--", end = "")


		# print alphabets in decreasing order
		for alp in range(i-1):  # alp = 0 1 2 ... i-1
			print(chr(ord('a') + n-1-alp),end ="-")

		# print alp in increasing order
		for alp in range(i-1):
			print(chr(ord('a') + n - i + alp),end='-') 

		# print last alphabet separately without --
		print(chr(ord('a')+n-1),end='')

		# print -- here again
		for s in range(n-i):
			print("--",end = '')

		# go to the new line
		print()


	for i in range(n-1, 0,-1): # printing in reverse order
		#first print --
		for s in range(n-i):
			print("--", end = "")


		# print alphabets in decreasing order
		for alp in range(i-1):  # alp = 0 1 2 ... i-1
			print(chr(ord('a') + n-1-alp),end ="-")

		# print alp in increasing order
		for alp in range(i-1):
			print(chr(ord('a') + n - i + alp),end='-') 

		# print last alphabet separately without --
		print(chr(ord('a')+n-1),end='')

		# print -- here again
		for s in range(n-i):
			print("--",end = '')

		# go to the new line
		print()
	
ans = alphabetic_pattern(n)