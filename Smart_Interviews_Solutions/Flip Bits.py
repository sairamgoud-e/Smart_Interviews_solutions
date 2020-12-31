t=int(input())
for i in range(t):
    a,b=input().split()
    a,b=str(bin(int(a)))[2:],str(bin(int(b)))[2:]
    #print(a,b)
    while len(a)!=len(b):
        if len(a)>len(b):
            b='0'+b
        if len(b)>len(a):
            a='0'+a
    c=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            c=c+1
    print(c)
            
            
                   
