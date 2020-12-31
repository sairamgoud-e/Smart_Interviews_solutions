t=int(input())
for i in range(t):
    n=int(input())
    b=bin(n)
    k=(str(b)[2:])
    #print(k)
    if len(k)%2!=0:
        k='0'+k
    #print(k)
    k=list(k)
    for i in range(1,len(k),2):
        #print(i)
        k[i],k[i-1]=k[i-1],k[i]
    
    #print(k)
    k=''.join(k)
    print(int(k, 2))
    #print(k)
        
        
   
