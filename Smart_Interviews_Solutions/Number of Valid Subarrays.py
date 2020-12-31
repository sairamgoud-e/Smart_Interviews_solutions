t=int(input())
for tx in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    #print(l)
    d={}
    s=0
    c=0
    
    def insert(k):
        if k in d.keys():
            d[k]=d[k]+1
        else:
            d[k]=1

    
    for i in l:
        if i==0:
            s=s-1
        else:
            s=s+i
        if s==0:
            c=c+1
        if s in d.keys():                #1001011    1,0,0    s=-1     c=0     d{1:1,0:1,-1:1}
            c=c+(d[s])
            #print(c)
        
        insert(s)
        
    #print(d)
    print(c)
        
        
            
