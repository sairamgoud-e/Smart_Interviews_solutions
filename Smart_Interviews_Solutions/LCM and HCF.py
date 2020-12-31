import math
t=int(input())
for i in range(t):
    #f=[]
    def lcm(a,b):
        if a<b:
            j=1
            while(a*j)%b!=0:
                j=j+1
            return (a*j)
            
        if b<a:
            j=1
            while(b*j)%a!=0:
                j=j+1
            return (b*j)
    
    def hcf(x,y):
        while(y):
            x, y = y, x % y
        return x
    
    a,b=map(int,input().split())
    if a==0 or b==0:
        print(0)
    else:    
        print(int((a*b)//(hcf(a,b))),end=' ')
    if a==0 or b==0:
        print(max(a,b),end=' ')
    else:
        if b>a:
            print(hcf(a,b))
        else:
            print(hcf(b,a))
    #print()
    #print(a,b,type(a))
    #print(int((a*b)/math.gcd(a,b)),math.gcd(a,b))
    
