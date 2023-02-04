def getTotalX(a, b):
    factores = 0
    i=1
    while i <= max(b):
        isFactor = True
        num=0
        while num < len(a) and isFactor == True:
            if i%a[num] != 0:
                i = i + 1
                isFactor = False
            else:
                num = num + 1
        if isFactor is not False:
            num2=0
            while num2 < len(b) and isFactor == True:
                if b[num2]%i!=0:
                    i =i + 1
                    isFactor = False
                else:
                    num2 =num2+ 1       
        if isFactor is True:
            factores =factores + 1
            i = i +1
    return factores 


if __name__ =="__main__":
    a=[2,4]
    b=[16,32,96]
    print("El nùmero de factores es {}".format(getTotalX(a,b)))