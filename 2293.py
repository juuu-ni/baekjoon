#1차원 DP
#dp[i] : 금액 i를 만드는 경우의 수
#초기상태 : dp[0] = 1
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])
