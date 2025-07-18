n = int(input())
cnt = 0 

while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        n = 0  
        break
    n -= 2
    cnt += 1

print(cnt if n == 0 else -1)
