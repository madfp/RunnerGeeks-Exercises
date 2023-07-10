import sys
import itertools

band = 0
control = 1
permutation = []
n = 0

# Entrada estandar
for i in sys.stdin:
    if band == 0:
        band = 1
        n = int(i)
    elif band == 1:
        permutation = i.replace(" ", "").rstrip("\n")
        break
resultado = list(itertools.permutations(permutation, n))
res = ""
for i in resultado:
    for j in i:
        res += j + " "
    res.rstrip(" ")
    sys.stdout.write(str(res))
    print("\n")
    res = ""