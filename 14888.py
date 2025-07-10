N = int(input())        #백준 14888번 dfs 사용문제
nums = list(map(int,input().split()))
opr = list(map(int,input().split()))

maxv = -1e9
minv = 1e9

def dfs(depth, total , sum, sub, mul, div): #depth개 숫자 사용 , 결과 total
    if depth== N :
        global maxv,minv
        maxv = max(maxv,total)
        minv = min(minv,total)
        return
    
    if sum:
        dfs(depth +1,total+nums[depth], sum-1,sub,mul,div)

    if sub:
        dfs(depth+1,total-nums[depth],sum,sub-1,mul,div)

    if mul:
        dfs(depth+1,total*nums[depth],sum,sub,mul-1,div)

    if div:
        if total<0:
            dfs(depth+1,-(-total//nums[depth]),sum,sub,mul,div-1)
        else:
            dfs(depth+1,total//nums[depth],sum,sub,mul,div-1)

dfs(1, nums[0], opr[0], opr[1], opr[2], opr[3])

print(maxv)
print(minv)
