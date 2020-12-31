t=int(input())
for i in range(t):
    a,b=input().split()
    if sorted(a)==sorted(b):
        print("True")
    else:
        print("False")
