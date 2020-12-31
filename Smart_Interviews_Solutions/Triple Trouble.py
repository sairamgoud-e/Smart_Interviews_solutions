t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=list(set(l))
    k.sort(reverse=True)
    l.sort()
    for i in k:
        if l.count(i)==1:
            print(i)
            break
        
