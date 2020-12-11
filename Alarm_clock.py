"""
Alarm Clock
Description
You're trying to automate your alarm clock by writing a function for it. 
You're given a day of the week encoded as 1=Mon, 2=Tue, ... 6=Sat, 7=Sun, and 
whether you are on vacation as a boolean value (a boolean object is either True or False. 
Google "booleans python" to get a better understanding). 
Based on the day and whether you're on vacation, 
write a function that returns a time in form of a string indicating when the alarm clock should ring. 

When not on a vacation, on weekdays, 
the alarm should ring at "7:00" and 
on the weekends (Saturday and Sunday) it should ring at "10:00". 

While on a vacation, it should ring at "10:00" on weekdays. 
On vacation, it should not ring on weekends, that is, it should return "off".

Input:
The input will be a list of two elements. 
The first element will be an integer from 1 to 7, and 
the second element will be a boolean value.

Output:
The output will be a string denoting the time alarm will ring or 'off'

input testcases: 
[1,False]
[3,True]
[7,True]

dict_1 = {1 : "Mon", 2 : "Tue", 3 : "Wen", 4 : "Thus", 5 : "Fri", 6 : "Sat", 7 : "Sun"}
"""
import random 
input_1 = random.choice([1,2,3,4,5,6,7]) # day number
input_2 = random.choice([True, False]) # On vacations

def alarmclock(input_1, input_2):
	if input_2 == True:
		if input_1 == 6 or input_1 == 7:
			return "off"
		else:
			return "10:00"

	else:
		if input_1 == 6 or input_1 == 7:
			return "10:00"
		else:
			return "7:00"

print(alarmclock(input_1, input_2))


