t=int(input())
for i in range(t):
    n=int(input())
    n=str(bin(n))[2:]
    #print(type(n))
    if n[0]=='1' and n.count('1')==1:
        print("True")
    else:
        print("False")
