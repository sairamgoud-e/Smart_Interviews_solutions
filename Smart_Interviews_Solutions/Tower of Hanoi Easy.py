t=int(input())
for i in range(t):
    n=int(input())
    def TowerOfHanoi(n , source, destination, auxilliary): 
        if n==1: 
            print ("Move 1 from",source,"to",destination)
            #cnt=cnt+1
            return
        TowerOfHanoi(n-1, source, auxilliary, destination) 
        print ("Move",n,"from",source,"to",destination) 
        TowerOfHanoi(n-1, auxilliary, destination, source) 
          
    #n = 4
    cnt=0
    def steps(n):
        return ((2**n)-1)
    print(steps(n))
    TowerOfHanoi(n,'A','C','B')  
