def ListComprehensions(x,y,z,n):
    data = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                data.append([i,j,k]) 
    
    datos = [x for x in data if (x[0]+x[1]+x[2])!= n]
    print(datos)

if __name__ =="__main__":
    ListComprehensions(1,1,2,3)