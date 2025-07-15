def fib(num):
    if num<2:
        return num
    
    return fib(num-1)+ fib(num-2)


num = int(input())
print(fib(num))