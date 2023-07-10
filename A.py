import sys

band = 0
cont = 0
control = 0
operations = []
signos = ["+", "-", "^", "*", " /"]

for i in sys.stdin:
    if band == 0:
        control = int(i)
        band = 1
    else:
        operations.append(i.rstrip("\n"))
        cont+=1
        if cont == control:
            break

subOperacion = ""
for operaciones in operations:
    operaciones = list(operaciones)
    listIndex = []
    openParentesis = False

    for k, char in enumerate(operaciones):
        if char == "(":
            openParentesis = True
            listIndex.append(k)
        elif openParentesis:
            if char == ")":
                listIndex.append(k)
                openParentesis = False
                subOperacion = list(subOperacion)
                cont = 0
                for j,char in enumerate(subOperacion):
                    if char in signos:
                        subOperacion.insert(0,subOperacion.pop(j))
                        cont += 1
                    print(subOperacion)
                subOperacion = ""
                listIndex =[]
            else:
                subOperacion += char