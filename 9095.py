#dp문제
T = int(input())
dp = [0] * 11   # dp[i] = i를 만드는 방법의 수 (최대 10)

#초기값
dp[1] = 1
dp[2] = 2
dp[3] = 4

#점화식
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#테스트 케이스마다 출력
for _ in range(T):
    n = int(input())
    print(dp[n])