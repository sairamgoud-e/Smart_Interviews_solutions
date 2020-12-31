import math
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    #e=int(n/5)
    while True:
        e=int(n/5)
        c=c+e
        n=e
        if e<5:
            break
    print(c)
    
    
    
    
