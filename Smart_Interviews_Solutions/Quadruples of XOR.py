t=int(input())
for tx in range(t):
    n=int(input())
    di={}
    dm={}
    cnt=0
    def insert(k):
        if k in di:
            di[k]=di[k]+1
        else:
            di[k]=1
    
    def ins(k):
        if k in dm:
            dm[k]=dm[k]+1
        else:
            dm[k]=1
    
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    for i in range(n):
        for j in range(n):
            s=a[i]^b[j]
            insert(s)
            ins(c[i]^d[j])
    for i in di:
        if i in dm:
            cnt=cnt+(dm[i]*di[i])
    
    print(cnt)
            
        
