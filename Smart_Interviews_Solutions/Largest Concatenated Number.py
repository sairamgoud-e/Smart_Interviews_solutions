from functools import cmp_to_key
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    #print ("The original list is : " + str(l))  
    res = sorted(l, key = cmp_to_key(lambda i, j: -1
                if str(j) + str(i) < str(i) + str(j) else 1)) 
    print (''.join(map(str,res))) 
