def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        ar = [0,0]
        
        
        if a[i] > b[i]:     
            alice += 1
        elif b[i] > a[i]:
            bob +=1
        else:
            continue
            
    return [alice, bob]
    
a,b = [1,2,3],[2,4,5]
    
print(compareTriplets(a,b))
            