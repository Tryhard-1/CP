"""
Problem: Codeforces 2277B - Sequence Decreasing
Status: Accepted

Core Idea:
- Each operation removes 1 element while decrementing a subarray.
- If the array doesn't already contain a 0, so for the full array to become zeros, 
  we'll do the operations and will try to make the minimum number of the array 0, 
  for which the minimum element must not exceed n - 1 decrements.

Complexity:
- Time: O(n) per test case, O(sum of n) total
- Space: O(n) to store the input list
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map (int, input().split()))
 
    if min(a) <= n-1:
        print(n)
    else:
        print(0) 