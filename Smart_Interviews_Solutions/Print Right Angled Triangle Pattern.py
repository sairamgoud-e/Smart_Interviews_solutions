n=int(input())
for k in range(n):
    s=int(input())
    print("Case #",end="")
    print(k+1,end="")
    print(":")
    for i in range(1,s+1):
        print(" "*(s-i),end="")
        print("*"*i)
        
        
