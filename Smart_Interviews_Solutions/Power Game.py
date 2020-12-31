t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    p1=0
    p2=0
    c=0
    l1.sort()
    l2.sort()
    while p1<n and p2<n:
        if l1[p1]>l2[p2]:
            p2=p2+1
            p1=p1+1
            c=c+1
        else:
            p1=p1+1
            
    print(c)
            
