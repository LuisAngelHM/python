def spaces(n, i):
    countSpace= n-i
    spaces = " "*countSpace   
    return spaces

def staircase(n):
    for i in range(1, n+1):
        cadena = spaces(n,i)
        steps = "#"*i
        cadena = cadena+steps 
        print(cadena)
    
if __name__ == "__main__": 
    tamanio = int(input("Ingresa el numero de escalones: "))
    staircase(tamanio)