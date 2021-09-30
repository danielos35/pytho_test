n = [2,3,6,6,5]

m = (sorted(n, reverse=True))

for i in range(len(m)):
    i+=1
    if m[i-1] == m[i]:
        continue
    else:
        print (m[i])
        break
        
    