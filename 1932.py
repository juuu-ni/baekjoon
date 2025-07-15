n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * n  # 크기를 n으로 맞춤
dp[0] = tri[0][0]

for i in range(1, n):
    for j in range(i, -1, -1):
        if j == 0:
            dp[j] = dp[j] + tri[i][j]
        elif j == i:
            dp[j] = dp[j - 1] + tri[i][j]
        else:
            dp[j] = max(dp[j - 1], dp[j]) + tri[i][j]

print(max(dp))
