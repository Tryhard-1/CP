'''
Problem: 266A - Stones on the Table
Status: Accepted

Core Idea:
- For every matching adjacent pair, one stone must be removed.
- Counting matching adjacent pairs yields the minimum number of stones to be removed.

Complexity:
- Time: O(n)
- Space: O(1)
'''

n = int(input())
c = input()

count = 0
for i in range(1,n):
    if c[i-1] == c[i]:
        count += 1
print(count)