# 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    if n==1 or n==2:
        return 1
    if n<6:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return fibonacci(n-1)+fibonacci(n-2)-fibonacci(n-5)

print fibonacci(10)

def spread(n,s,t):
    if n>=t:
        return 0
    else:
        return 1+spread(n*(1+s),s,t)

print spread(1,2,10)
#print fibo(2)