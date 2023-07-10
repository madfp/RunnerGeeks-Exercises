import sys
info = []
band = 0

for i in sys.stdin:
    if band == 0:
        band = 1
        info.append(i)
    elif band == 1:
        info.append(str(i).rstrip("\n").split(" "))
        band = 2
    else:
        info.append(i)
        break

n = info[0]
an = [int(elements) for elements in info[1]]
x = info [2]

def horner(lista):
    if len(lista) == 1:
        return int(lista[0])
    else:
        return int(lista[0]) + int(x)*horner(lista[1:])

sys.stdout.write(str(horner(an)))