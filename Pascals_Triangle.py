"""
Pascal's Triangle

Description
A pascal's triangle is a very interesting mathematical concept.
Each number here is a sum of the two numbers directly above it.
Following is an 8 level Pascal's triangle:﻿
﻿
You can read about Pascal's triangle here.
Your task is to print an nth level of Pascal's triangle.
The input will contain an integer n.
The output will contain 1 line of the list of numbers representing the nth row of Pascal's triangle.

Sample Input:
6
Sample Output:

[1, 5, 10, 10, 5, 1]
"""
import random
n= random.choice([3,4,5,6,7,8,9,10])

Pascals=[[1 for i in range(j)] for j in range(1, n+1)]

for i in range(2, n):
    for j in range(1,i):
        Pascals[i][j]=Pascals[i-1][j-1]+Pascals[i-1][j]
        

print(Pascals[-1]) 