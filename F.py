#Importamos los módulos y librerías necesarios
from sys import stdin, stdout
info = []

#Entrada estandar y lectura de datos
for i, input in enumerate(stdin):
    if i == 0:
        continue
    elif i == 1:
        info.append(str(input).rstrip("\n").split(" "))
    else:
        info.append(input)
        break

#Inicializamos variables
an = [int(elements) for elements in info[0]]
x = int(info[1])

#Función recursiva aplicando la regla de Horner
def horner(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + x * horner(lista[1:])

#Salida estandar
stdout.write(str(horner(an)))