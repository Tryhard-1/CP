'''
Problem: 231A - Team
Status: Accepted

Core Idea:
- For each problem, if the sum of confidence scores is atleast 2, increase the count.

Complexity:
- Time: O(n)  
- Space: O(1)
'''


n = int(input())
c = 0
for _ in range(n):
    l = list(map(int,input().split()))
    if sum(l)>=2:
        c += 1

print(c)
