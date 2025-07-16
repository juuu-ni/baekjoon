A,B,C,M = map(int,input().split())
piro = 0
work = 0

for _ in range(24):
    if piro + A <=M:
        piro +=A
        work +=B
    else:
        piro -=C
        if piro < 0:
            piro = 0

print(work)
