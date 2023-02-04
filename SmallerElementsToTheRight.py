def SmallerElements(numarray):
    numarray2 = list()
    for i in range(len(numarray)):
        cantidad = 0
        for j in range(i, len(numarray)):
            if numarray[i] > numarray[j]:
                cantidad = cantidad + 1
        numarray2.append(cantidad)
    return numarray2


if __name__ == "__main__":
    numeros = [85,4000,2,1,1]
    print(SmallerElements(numeros))