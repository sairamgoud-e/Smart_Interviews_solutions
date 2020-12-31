n=int(input())
#for tx in range(t):
l=list(map(int,input().split()))
d={}
def insert(k):
    if k in d:
        d[k]=d[k]+1
    else:
        d[k]=1
    
for i in l:
    insert(i)
nq=int(input())
for j in range(nq):
    q=int(input())
    if q in d:
        print(d[q])
    else:
        print(0)
    
    
        
