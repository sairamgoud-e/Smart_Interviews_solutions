t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    #print(n,k)
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    #print(l)
    b=0
    c=0
    f=1
    while c<n and f<n:
        if l[b]-l[f]<k:
            f=f+1
            #continue
        elif l[b]-l[f]>k:
            b=b+1
        elif l[b]-l[f]==k and c!=f:
            print("true")
            c=1
            break
    if c==0:
        print("false")
            
