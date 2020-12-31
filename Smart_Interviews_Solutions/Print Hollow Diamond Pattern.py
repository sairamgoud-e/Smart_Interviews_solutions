t=int(input())
for i in range(t):
    n=int(input())
    k=int(n/2)
    print("Case #%s:"%(i+1))
    for i in range(0,n):
        if i==0:
            print((k-i)*' '+'*')
            continue
        if i<=k:
            print((k-i)*' '+'*'+((i*2)-1)*' '+'*')
        if i==n-1:
            print((i-k)*' '+'*')
            break
        if i>k:
            print((i-k)*' '+'*'+((((n-1)-i)*2)-1)*' '+'*')
