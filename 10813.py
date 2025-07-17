"""
1 2 3 4 5
2 1 3 4 5
2 1 4 3 5
3 1 4 2 5
"""

N,M = map(int,input().split())
nums= []
for i in range(N):
    nums.append(i+1)

change = [list(map(int,input().split())) for _ in range(M)]

for a,b in change:
    nums[a-1],nums[b-1] = nums[b-1],nums[a-1]

print(*nums)


