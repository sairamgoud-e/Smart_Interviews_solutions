t=int(input())
for i in range(t):
    l1=[]
    l2=[]
    m1,n1=map(int,input().split())
    for i in range(m1):
        l=list(map(int,input().split()))
        l1.append(l)
    m2,n2=map(int,input().split())
    for i in range(m2):
        l=list(map(int,input().split()))
        l2.append(l)
    #print(l1)
    #print(l2)
    res=[]
    for i  in range(m1):
        t=[]
        for j in range(n2):
            t.append(0)
        res.append(t)
    #print(res)
    #print(len(l1))
    #print(len(l2))
    for i in range(len(l1)):  
        for j in range(len(l2[0])):  
            for k in range(n1):  
                res[i][j] += l1[i][k] * l2[k][j]  
    for i in res:
        for j in i:
            print(j,end=' ')
        print()
        
        #print(i)
        #print()"""
    
