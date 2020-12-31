
t=int(input())
#top=0
for i in range(t):
    n=int(input())
    stk=[]
    #top=0
    mx=[]
    print("Case "+str(i+1)+":")
    for j in range(n):
        inp=list(input().split())
        op=inp[0]
        #print(inp)
        if op=='A':
            #print(op)
            ele=int(inp[1])
            if len(stk)==0:
                stk.append(ele)
                mx.append(ele)
                #top=0
            elif ele >=(mx[-1]):
                #print(ele,stk[-1])
                stk.append(ele)
                mx.append(ele)
                #top=top+1
            elif ele<mx[-1]:
                mx.append(mx[-1])
                stk.append(ele)
                #top=top+1
        elif op=='Q':
            if len(stk)==0:
                print("Empty")
            else:
                print(mx[-1])
        elif op=='R':
            if len(stk)>0:
                stk.pop(-1)
                mx.pop(-1)
        #print(stk,mx)
        
            
    
