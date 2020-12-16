"""
Lego Stack

Description
You are given a row of Lego Blocks consisting of n blocks. 
All the blocks given have a square base whose side length is known. 
You need to stack the blocks over each other and create a vertical tower. 
Block-1 can go over Block-2 only if sideLength(Block-2)=>sideLength(Block-1).
From the row of Lego blocks, you can only pick up either the leftmost or rightmost block.
Print "Possible" if it is possible to stack all n cubes this way or else print "Impossible".

Input Format:

The input will contain a list of n integers representing the side length of each 
block's base in the row starting from the leftmost

Sample Input:

[5 ,4, 2, 1, 4 ,5]

Sample Output:

Possible
"""

input_list = [5 ,4, 2, 1, 4 ,5]


#def Lego_stack(input_list):

tower = []

while input_list:

	if input_list[0] >= input_list[-1]:
		tower.append(input_list[0])
		input_list.pop(0)

	else:
		tower.append(input_list[-1])
		input_list.pop(-1)

flag = 1
for i in range(1, len(tower)):
	if tower[i-1] < tower[i]:
		print("Impossible")
		flag = 0
		break

if flag == 1:
	print("Possible")




