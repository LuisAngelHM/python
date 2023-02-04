def NestedList(lista):
    lista.sort(key=lambda x: x[1])
    names = []
    i = 0
    tam = len(lista)-1
    cont = True
    while i < tam and cont is True:
        if lista[i][1]!=lista[i+1][1]:
            cont = False
        i = i+1
    cont = True
    names.append(lista[i][0])
    while i < tam and cont is True:
        if lista[i][1]==lista[i+1][1]:
            names.append(lista[i+1][0])
        else:
            cont = False
        i = i+2
    names.sort()    
    print(names)


if __name__ == "__main__":
    notes = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.1],["trina",37.15] ,['Akriti', 41], ['Harsh', 39]]
    NestedList(notes)