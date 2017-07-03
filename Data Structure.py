import urllib

def getpage(url):
    """This Code is working right"""
    try:
        return urllib.urlopen(url).read()
    except Exception, Argument:
        return Argument

def get_next_target(page):
    """This is working fine"""
    try:
        start_link = page.find("<a href=")
        if start_link == -1:
            return None,0
        start_quote = page.find('"',start_link)
        end_quote = page.find('"',start_quote+1)
        url = page[start_quote+1:end_quote]
        return url, end_quote
    except Exception,Argument:
        print "Get next target error ",Argument

def get_all_links(page):
    """This is working fine"""
    links=[]
    try:
        while True:
            url, endpos=get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                break
        return links
    except Exception,Argument:
        print "Get all links error",Argument

def union(p,q):
    """This is working right"""
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
    to_crawl=[seed]
    crawled=[]
    index={}
    graph={}
    n=0
    while to_crawl and n<3:
        print "Execution number : ",n
        page = to_crawl.pop()
        if page not in crawled:
            content = getpage(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            if(outlinks!=None):
                union(to_crawl, outlinks)
            crawled.append(page)
        n+=1
    return index, graph

def record_user_click(index,key,url):
    urls=look_up(index,key)
    if urls:
        for entry in urls:
            if entry[0]==url:
                entry[1]=entry[1]+1

def add_to_index(index,key,url):
    if key in index:
        if url not in index[key]:
            index[key].append(url)
    else:
        index[key] = [url]


def look_up(index,key):
    if key in index:
        return index[key]
    return None

def lucky_search(index,ranks,key):
    pages=look_up(index,key)
    if not pages:
        return None
    bestpage=pages[0]
    for candidate in pages:
        if ranks[candidate]>bestpage:
            bestpage=candidate
    return bestpage

def add_page_to_index(index,url,content):
    list=split_string(content,[","," ","/"," '",'"',".",">","<","[","]",";",":","{","}","|","!","#","@","$","%","^","&","*","(",")"])
    #list=content.split()
    for word in list:
        add_to_index(index,word,url)

def compute_graph(graph):
    d=0.8 #Damping Factor
    numloops=10
    ranks={}
    npages=len(graph)
    for page in graph:
        ranks[page]=1.0/npages
    for i in range(0,numloops):
        newranks={}
        for page in graph:
            newrank=(1-d)/npages
            for node in graph:
                try:
                    if page in graph[node]:
                        newrank=newrank+d*(ranks[node])/len(graph[node])
                except:
                    return
            newranks[page]=newrank
        ranks=newranks
    return ranks

def split_string(source,splitlist):
    output=[]
    atsplit=True
    for char in source:
        if char in splitlist:
            atsplit=True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                #print output[-1],type(output[-1])
                try:
                    output[-1] = str(output[-1])+char
                except Exception,Arg:
                    return "Error from split string ",Arg
    return output

"""def make_string(p):
    s="".join(p)
    return s"""

"""def make_big_index(size):
    index=[]
    letters=['a','a','a','a','a','a','a','a']
    while len(index)<size:
        word=make_string(letters)
        add_to_index(index,word,"fake")
        for i in range(len(letters)-1,0,-1):
            if letters[i] < 'z':
                letters[i]=chr(ord(letters[i])+1)
                break
            else:
                letters[i]='a'
    return index"""

"""def time_execution(code):
    start=time.clock()

    run_time=time.clock()-start
    return run_time"""

#print time_execution('make_big_index(10000)')

index,graph=crawl_web("http://www.axelta.com/")
print "Executing compute graph now"
print compute_graph(graph)