t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=[]
    sp=[]
    #sp=0
    s.append(0)
    for i in range(0,n):
        while (len(s)!=0 and l[s[-1]]<=l[i]):
            s.pop()
        if (len(s)==0):
            sp.append(i+1)
        else:
            sp.append(i-s[-1])
        s.append(i)
    for i in range(len(sp)):
            print(sp[i],end=' ')
    print()
        

        
