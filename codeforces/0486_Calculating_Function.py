'''
Problem: 486A - Calculating Function
Status: Accepted

Core Idea: 
- Calculate f(n) = - 1 + 2 - 3 + ... + (-1)^n * n
- When n is even, f(n) evaluates to n//2
- When n is odd, f(n) evaluates to n//2 - n

Complexity:
- Time: O(1)
- Space: O(1)
'''

n = int(input())
if n%2 == 0:
    print(n//2)
else:
    print(n//2 - n)