t=int(input())
for tx in range(t):
    s=input()
    l=list(s)
    c=0
    n=len(l)
    for i in range(n):
        if l[i] in l[i+1:n+1]:
            print(l[i])
            c=c+1
            break
    if c==0:
        print('.')
