def stamp(n):
    f=n/5
    t=(n-(f*5))/2
    o=n-((f*5)+(t*2))
    return f,t,o

#print stamp(5)

def bigger(a,b):
    if a>b:
        return a
    else:
        return b

def biggest(a,b,c):
    result=bigger(a,bigger(b,c))
    return result

def smaller(a,b):
    if a>b:
        return b
    else:
        return a

def smallest(a,b,c):
    result =smaller(a,smaller(b,c))
    return result

def range(a,b,c,):
    return biggest(a,b,c)-smallest(a,b,c)

#print range(10,4,7)

def fix_margin(s1,s2):
    n=0
    c=0
    while (n<len(s2)):
       if s2[n] in s1:
           c+=1
           n+=1

       else:
           break

    if c==len(s2):
        print "Don't give me something useless next time"
    else:
        print s2

fix_margin("Mohit Motwani","wani")

