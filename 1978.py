N = int(input())
nums = list(map(int, input().split())) 
cnt = 0

for num in nums:
    if num == 2:
        cnt += 1
    elif num % 2 != 0:
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2): 
            if num % i == 0:
                is_prime = False
                break
        if num > 1 and is_prime:
            cnt += 1

print(cnt)
