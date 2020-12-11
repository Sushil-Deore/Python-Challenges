"""
Arithematic Progression

Description
In mathematics, an arithmetic progression (AP) or arithmetic 
sequence is a sequence of numbers such that the difference 
between the consecutive terms is constant. The difference 
here means the second minus the first. For instance, 
sequence 5, 7, 9, 11, 13, 15, . . . is an arithmetic 
progression with common difference of 2.
Given any three terms of some random Arithematic progression 
and an integer key, you have to determine if the key will be 
present in the Arithematic sequence or no. check out sample 
input/output for more clarification.

Input:
The first line will contain three comma-separated integers 
representing three consecutive of some Arithmetic Progression
The second line will have the integer key

Output:
True if the key is a part of that AP, False otherwise

Sample input:
9, 11, 13
19

Sample output:
True

Sample input:
9, 11, 13
20

Sample output:
False

Sample input:
9, 11, 13
3

Sample output:
True
"""
input_list = [9, 11, 13]

input_key = 3

a = input_list[0]
b = input_list[1]
c = input_list[2]

common_diff = b - a 

if a % common_diff == input_key % common_diff:
	print(True)
else:
	print(False)

"""
Option 2

def arithmatic_progression(input_list, int_key):

    input_list.sort()
    
    com_diff = input_list[1] - input_list[0]
        
    if int_key > int(input_list[0]):
        for i in range(2, len(input_list)):
            if com_diff == 0:
                return int_key == input_list[i]
            else:
                return((int_key - input_list[0]) % com_diff==0) and int((int_key - input_list[0])/ com_diff) >= 0
                
    else:
        return ((input_list[0] - int_key) % com_diff == 0) and int((input_list[0] - int_key) / com_diff) >= 0
    
print(arithmatic_progression(input_list, int_key))
"""