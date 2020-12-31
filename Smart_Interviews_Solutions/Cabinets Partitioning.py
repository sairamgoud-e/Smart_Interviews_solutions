import math
res=[]
t=int(input())
for tx in range(t):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    #print(n,k)
    #print(li)
    def f(li,m):
        s=0
        c=1
        i=0
        while i<(len(li)):
            if (s+li[i])<=m:
                s=s+li[i]
                i=i+1
            else:
                c=c+1
                s=0
        return (c)        

    #print(f(54))
    l=max(li)
    h=sum(li)
    while l<=h:
        mid=math.floor((l+h)/2)
        if f(li,mid)<=k:
            h=mid-1
        else:
            l=mid+1
    print(l)
    
    
    
    
