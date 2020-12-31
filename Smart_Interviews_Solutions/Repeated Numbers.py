t=int(input())
for tx  in range(t):
    n=int(input())
    re=[]
    l=list(map(int,input().split()))
    #print(l)
    l.sort()
    for i in range(1,len(l)):
        if l[(i-1)]==l[i]:
            re.append(l[(i-1)])
    re=list(set(re))
    re.sort()
    for i in re:
        print(i,end=' ')
    print()
