def producto(arraynumber):
    product = 1
    new_arrat = list()
    for i in arraynumber:
        product = product * i
    
    for i in arraynumber:
        new_product = product / i
        new_arrat.append(int(new_product))
    return new_arrat


if __name__ == "__main__":
    numeros = [1,2,3,4,5]
    print(producto(numeros))