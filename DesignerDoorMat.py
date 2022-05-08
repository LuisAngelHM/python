import math

def print_dash(n):
    return int(n)*'-'

def print_decorators(n):
    return int(n)*".|."

def designerDoorMat(n,m):
    cadena = ''
    for i in range(1,(n//2)+1):
        number_decorations = (2*(i-1))+1
        dashs = print_dash((m-(3*number_decorations))/2)
        center = print_decorators(number_decorations)
        cadena = cadena +dashs+center+dashs + '\n'
    dashs = print_dash((m-(7))/2)
    center = 'WELCOME'
    cadena = cadena +dashs+center+dashs+ '\n'
    for i in range((n//2),0,-1):
        number_decorations = (2*(i-1))+1
        dashs = print_dash((m-(3*number_decorations))/2)
        center = print_decorators(number_decorations)
        cadena = cadena +dashs+center+dashs+ '\n'
    return cadena

if __name__ == '__main__':
    data = input()
    data = data.split()
    try:
        n = int(data[0])
        m = int(data[1])
        print(designerDoorMat(n,m))
    except:
        pass

    
