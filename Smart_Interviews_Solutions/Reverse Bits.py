t= int(input())
for i in range(t):
    n=int(input())
    n=str(bin(n))[2:]
    d=32-len(n)
    n=('0'*d)+n
    #print(n)
    n=n[::-1]
    print(int(n,2))
