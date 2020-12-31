n=int(input())
stk=[]
for i in range(n):
    inp=list(input().split())
    #print(inp)
    p=inp[0]
    #print(p,k)
    
    
    def push(k):
        stk.append(k)
        #print(stk)
        
    def popp():
        if len(stk)==0:
            print("Empty")
        else:
            print(stk.pop())
            
    if p=="push":
        ele=inp[1]
        ele=int(ele)
        #print(ele)
        push(ele)
    else:
        popp()
        
        
