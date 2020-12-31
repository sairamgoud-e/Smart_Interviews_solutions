

def insert(a,d):
    if a in d:
        d[a]=d[a]+1
    else:
        d[a]=1
def delete(a,d):
    if a in d:
        d[a]=d[a]-1
        if d[a]==0:
            del d[a]
        
        
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    h={}
    
    for i in range(k):
        insert(l[i],h)
    print(len(h),end=" ")
    #print(h)
    s=0
    e=i+1
    while e<n:
        insert(l[e],h)
        delete(l[s],h)
        #print(h)
        print(len(h),end=" ")
        e=e+1
        s=s+1
    print()
        
    
        
