import time
import HashTable

def time_execution(code):
    start=time.clock()
    result = eval(code)
    run_time=time.clock()-start
    return result,run_time

def shift_n_interval(c,l):
    return chr(ord(c)+(l))

#print shift_n_interval('s',-10)

def rotate(s,l):
    st=[]
    for c in s:
         st.append(chr(ord(c)+(l)))
    S="".join(st)
    return S

def crawl_web(seed):
    to_crawl=[seed]
    crawled=[]
    index={}
    while to_crawl:
        page=to_crawl.pop()
        if page not in crawled:
            content=getpage(page)
            add_page_to_index(index,page,content)
            union(to_crawl,get_all_links(content))
            crawled.append(page)
    return index

