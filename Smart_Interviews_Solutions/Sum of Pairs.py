t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    p1=0
    p2=n-1
    c=0
    l.sort()
    while p1<p2:
        if l[p1]+l[p2]<k:
            p1=p1+1
        elif l[p2]+l[p1]>k:
            p2=p2-1
        elif l[p1]+l[p2]==k:
            print("True")
            c=1
            break
    if c==0:
        print("False")
            
