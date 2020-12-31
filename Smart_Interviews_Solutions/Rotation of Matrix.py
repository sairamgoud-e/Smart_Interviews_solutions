t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    for j in range(n):
        l1=list(map(int, input().split()))
        l.append(l1)
    print("Test Case #%s:"%(i+1))
    #print(l)
    #for k in range(n):
    for m in range(n):
        for p in range(n-1,-1,-1):
            print(l[p][m],end=' ')
        print()
    
