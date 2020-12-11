"""
Above Average
Description

Finding the average of the data and comparing it with other 
values is often encountered while analysing the data. 
Here you will do the same thing. The data will be provided 
to you in a list. You will also be given a number check.  
You will return whether the number check is above average or no.

Input:
A list with two elements:
The first element will be the list of data of integers and
The second element will be an integer check.

Output:
True if check is above average and False otherwise

Sample input:
[ [2,4,6,8,10],  4]

Sample output:
False

Sample input:
[ [2,4,6,8,-10],  4]

Sample output:
True
"""

input_list = [[5,6,7,8,9], 7]

list_1 = input_list[0]
check = input_list[1]

avg = sum(list_1)/len(list_1)

if check > avg:
	print('True')

else:
	print('False')