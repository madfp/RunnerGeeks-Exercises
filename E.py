#Importamos los módulos y librerías necesarios
from sys import stdin, stdout; from itertools import permutations

# Entrada estandar
for i, input in enumerate(stdin):
    if i == 0:
        n = int(input)
    else:
        permutacion = input.replace(" ", "").rstrip("\n")
        break;

#Calculamos las permutaciones de la secuencia de números
resultado = list(permutations(permutacion, n))

#Imprimimos las permutaciones en orden
for i in resultado:
    res = " ".join([numero for numero in i]).rstrip(" ")
    stdout.write(str(res) + "\n")    