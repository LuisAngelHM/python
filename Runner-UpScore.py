from audioop import reverse


def runenerUpScore(lista):
    lista.sort(reverse=True)
    print(lista)
    continue_w =True
    i=0 
    rang=len(lista)-1
    while i <= rang and continue_w==True:
        if lista[i] !=lista[i+1]:
            print(lista[i+1])
            continue_w=False
        i += 1

if __name__ == "__main__":
    lista = [2,3,6,6,7,5]
    runenerUpScore(lista)