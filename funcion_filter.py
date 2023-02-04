'''
Verifica que los elementos de una secuencia cumplen un condición
devolviendo un iterador con los elementos que cumplen dicha condicion
Ejemplo

Programa que indica cuales son los números pares de una lista(array)
'''

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)


listaEmpelados = [
    Empleado("Juan", "Director", 75000),
    Empleado("Ana", "Presidencia", 85000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria",27000),
    Empleado("Mario", "Botones", 21000)
]

salarios_altos = filter(lambda empleado : empleado.salario > 50000, listaEmpelados)
for salario_alto in salarios_altos:
    print(salario_alto)