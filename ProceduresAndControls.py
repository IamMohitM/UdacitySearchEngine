def get_next_target(page):
    start_link=page.find("<a href=")
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_link+1)
    url=page[start_quote+1:end_quote]

    return url,end_quote

def rest_string(s):
    return s[1:]

def sum(a,b):
    a=a+b;
   # return a;

def abbaize(a,b):
    return a+b*2+a

sent="Mohit Motwani tomorrow is better than Mohit Motwani Yesterday"

def find_sec(a,b):
    first=a.find(b)
    return a.find(b,first)

print find_sec(sent,"Motwani")
#print rest_string("Mohit")
a=5
b=1

def is_friend(a):
    return a[0]=="D" or a[0]=="N"




print is_friend("Dixit")





#sum(a,b)
print abbaize("a","b")
print abbaize("mohit","mo")