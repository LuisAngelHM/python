def minMax(arr):
    sumaTotal = sum(arr)
    sumaMinima = sumaTotal
    sumaMaxima = 0
    for i in arr:
        if sumaTotal-i > sumaMaxima :
            sumaMaxima = sumaTotal-i
        if sumaTotal-i < sumaMinima:
            sumaMinima = sumaTotal-i
    print(sumaMaxima, sumaMinima)


if __name__ == "__main__":
    listaNumeros = [769082435, 210437958, 673982045, 375809214, 380564127]
    minMax(listaNumeros)

