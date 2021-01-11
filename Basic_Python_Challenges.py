# Print Hello, World!
print("Hello, World!")

# Given an integer,n, perform the following conditional actions:
-- If n is odd, print Weird
-- If n  is even and in the inclusive range of 2 to 5, print Not Weird
-- If n is even and in the inclusive range of 6 to 20, print Weird
-- If n is even and greater than 20, print Not Weird

if n%2 == 1:
    print('Weird')
elif n >= 2 and n <= 5:
    print('Not Weird')
elif n >= 6 and n <=20:
    print('Weird')
else:
    print('Not Weird')
    
# The provided code stub reads two integers from STDIN, a and.
# Add code to print three lines where: 
#  1.  The first line contains the sum of the two numbers.
#  2.  The second line contains the difference of the two numbers
#  3.  The third line contains the product of the two numbers

print(a + b)  
print(a - b)  
print(a * b)

# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division a//b
# The second line should contain the result of float division, a/b
# No rounding or formatting is necessary. 

print(a//b)
print(a/b)

# The provided code stub reads an integer, n, from STDIN.
# For all non-negative integers i<n, print i squared.

i = 0
while i < n:  
    print(i ** 2)
    i += 1
 