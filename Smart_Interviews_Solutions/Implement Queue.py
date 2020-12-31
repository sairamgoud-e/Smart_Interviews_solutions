n=int(input())
stk=[]

#fr=-1
#rr=-1

        
def deq(fr,rr):
        print(fr,rr)
        if rr==fr:
            print("Empty")
        else:
            rr=rr+1
            print(stk[rr])
            
for i in range(n):
    inp=list(input().split())
    p=inp[0]
    #print(fr,rr)
    
    
        
    

    
    
    if p=="Enqueue":
        ele=inp[1]
        ele=int(ele)
        stk.append(ele)
    else:
        if len(stk)==0:
            print("Empty")
        else:
            print(stk.pop(0))
        
        
