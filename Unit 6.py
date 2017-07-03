def fibonacci(n):
    if n==1 or n==2:
        return 1
    if n<6:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return fibonacci(n-1)+fibonacci(n-2)-fibonacci(n-5)

def spread(n,s,t):
    if n>=t:
        return 0
    else:
        return 1+spread(n*(1+s),s,t)

def is_list(p):
    return isinstance(p,list)

def deep_count(p):
    len=0
    for entry in p:
        len+=1
        if is_list(p):
            sum+=deep_count(p)
    return sum
