t=int(input())
for i in range(t):
    n=int(input())
    c=0
    l=list(map(int,input().split()))
    for j in range(0,n):
        for i in range(1,n-j):
            if l[i-1]>l[i]:
                l[i-1],l[i]=l[i],l[i-1]
                c=c+1
    #print(l)
    print(c)
