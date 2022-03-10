def countApplesAndOranges(s, t, a, b, apples, oranges):
    #s = inicio de la casa
    #t = fin de la casa
    #a = ubicacion del arbol de manzana
    #b = ubicacion del arbol de naranja
    #apples and oranges = arreglos de la distancia en x
    num_apples = 0
    num_oranges = 0
    for i in apples:
        if i + a >= s and i + a <= t:
            num_apples +=1 

    print(num_apples)

    for i in oranges:
        if i + b >= s and i + b <= t:
            num_oranges +=1
    print(num_oranges)

if __name__ == "__main__":
    countApplesAndOranges(7,11,5,15,[-2,2,1], [5,-6])