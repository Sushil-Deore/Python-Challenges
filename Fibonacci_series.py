"""
Fibonacci Series
Description
Compute and display Fibonacci series upto n terms where n is a positive integer entered by the user.

Fibonacci series.
Sample Input:
5
Sample Output:
0
1
1
2
3
"""
#input  
n = 5
"""
def fibonacci_number(n):
  a = 0
  b = 1
  if n < 0:
    print("Incorrect input")
  elif n == 0:
    return a 
  elif n == 1:
    return b
  else:
    for i in range(2,n):
      c = a + b
      a = b
      b = c
    return b
print(fibonacci_number(n))

"""
a = 0
b = 1
if n < 0:
  print("Incorrect input")
elif n == 0:
  print(a)
  
elif n == 1:
  print(a)
  
else:
  print(a)
  print(b)
  for i in range(2,n):
    c = a + b
    print(c)
    a = b
    b = c