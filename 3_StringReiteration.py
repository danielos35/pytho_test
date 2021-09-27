a = s
b = sorted(a)
c = ""
d = []
e = []


# List to String
for i in range(len(b)):
    c = str(c)+str(b[i])
    
    
#Alphabetical order 
for j in range(len(c)):
    if c[j] == "" or c[j] == c[j-1]:
        continue
    elif c[j]!= c[j-1]:
        contador = c.count(c[j])
        
        d.append(str(c[j])+" "+str(contador) )
        # print(c[j] , " " , contador)
        
        e.append(str(contador))





# Order Max to Min

e = sorted(e, reverse=True)


finalList = []

for i in range(len(d)):

    
    for j in range(len(d)):
        
        if (e[i] == d[j][2]) or (e[i][0] == d[j][2] and e[i][1] == d[j][3]) :
            if d[j] in finalList:
                continue
            else:
                finalList.append(d[j])
                break
                
        
    
    
print(finalList)
for i in range(3):
    print(finalList[i])     
    
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            # if e[i] == d[j][2]:
            #     if d[j-1][0]!= d[j][0] and d[-j][0]== d[j][0]:
            #         print(d[j])
            #         break
            #     else:
            #         continue
                    
            # else:
            #     continue
        