S = int(input())        #백준 1789번 그리디 사용문제

total = 0
n = 0

while total + (n + 1) <= S:
    n += 1
    total += n

print(n)