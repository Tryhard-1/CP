'''
Problem: 4A - Watermelon
Status: Accepted

Core Idea:
- Need to divide into two positive even numbers
- The sum of two evens is always even, so w should be even.

Gotchas: 
- w = 2 is even but it can't be divided into two evens.

Complexity:
- Time: O(1)
- Space: O(1)
'''

w = int(input())

if w==2:
    print("NO")
elif w%2==0:
    print("YES")
else:
    print("NO")
