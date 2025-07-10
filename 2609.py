a,b = map(int,input().split())  #백준 2609번 최대공약수 , 최소공배수

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd(a, b))
print(a*b // gcd(a, b))