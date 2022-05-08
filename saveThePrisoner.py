def saveThePrisoner(n,m,s):
    if (m+s-1)%n == 0:
        return n
    else: 
        return (m+s-1)%n 


if __name__ =="__main__":
    print(saveThePrisoner(5,2,1))
    print(saveThePrisoner(5,2,2))
    print(saveThePrisoner(7, 19, 2))
    print(saveThePrisoner(514824323, 514824324, 514824323))