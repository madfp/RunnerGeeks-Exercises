from sys import stdin, stdout

# Entrada de datos
for k, inputs in enumerate(stdin):
    if k == 0:
        cantidad = int(inputs.rstrip("\n"))
    elif k == 1:
        listNums = [int(numbers) for numbers in inputs.rstrip("\n").split(" ")]
    else:
        numFind = int(inputs.rstrip("\n"))
        break

# Ordenamos la lista de forma ascendente
listNums.sort()
count = 0
# l es el primer valor de la lista y r el ultimo
l, r = 0, len(listNums)-1
# Calculamos m1 y m2
m1 = int(l + (r-l)/3)
m2 = int(r - (r-l)/3)

index = -1

while l <= r:
    # Definimos las condiciones para retornar el indice encontrado
    if listNums[m1] == numFind:
        index = m1
        break
    elif listNums[m2] == numFind:
        index = m2
        break

    # Definimos las condiciones para actializar los valores
    if numFind < listNums[m1]:
        r = m1-1
    elif numFind < listNums[m2]:
        l = m2+1
    elif listNums[m1] < numFind and numFind > listNums[m2]:
        l = m1 + 1
        r = m2-1

    # Recalculamos para la siguiente vuelta los valores de m1 y m2
    m1 = int(l + (r-l)/3)
    m2 = int(r - (r-l)/3)

stdout(str(index))
