t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    re=[]
    for i in range(1,len(l)):
        temp=l[0:i+1]
        #temp.append(l[i])
        temp.sort()
        c=temp.count(l[i])
        #print(c)
        re.append((temp.index(l[i])+(c-1)))
        
    for i in re:
        print(i,end=' ')
    print()
        
