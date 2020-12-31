t=int(input())
for tx in range(t):
    n=int(input())
    l=[]
    re=[]
    for j in range(n):
        e=list(map(int,input().split()))
        l.append(e[::-1])
    #print(l)
    for i in range((n*2)-1):
        re.insert(i,[])
    #print(re)
    for i in range(n):
        for j in range(i,i+n):
            re[j].append(l[i][j-i])
    #print(re)
    for i in re:
        print(sum(i),end=' ')
    print()
