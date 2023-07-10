from sys import stdin, stdout


def preOrder(listChar: list[str]):
    listSimbols = ["-", "^", "+", "*", "/"]
    newList = [k for k in listChar]
    for k in range(len(newList)):
        if newList[k] in listSimbols:
            newList.insert(0, newList.pop(k))

    return newList


operations = []
signos = ["+", "-", "^", "*", " /"]

for k, input in enumerate(stdin):
    if k == 0:
        control = int(input)
        band = 1
    else:
        operations.append(input.rstrip("\n"))
        if k == control:
            break

signos = ["-", "+", "/", "*", "^"]

# Recorremos la lista de operaciones ingresasdas
for indice, operaciones in enumerate(operations):
    # Inicializamos variables
    foundBrackets = False
    listChar = list(operaciones)
    subOperacion = []
    indexInicial = 0
    # Recorremos los caracteres
    for k, char in enumerate(listChar):
        # Evaluamos si es una apertura de parentesis
        if char == "(":
            foundBrackets = True
            indexInicial = k+1
        elif char == ")":
            foundBrackets = False
            # Cuando encontramos el parentesis de cierre aplicamos el algoritmo de preorden y postorder
            operationPreOrder = preOrder(subOperacion)
            for j, caracter in enumerate(operationPreOrder):
                listChar[indexInicial+j] = caracter
            subOperacion = []
        elif foundBrackets:
            subOperacion.append(char)
        elif not foundBrackets and char in signos:
            listChar.insert(0, listChar.pop(k))

    print(f"{indice+1} Original: {''.join(a for a in operaciones)}")
    print(
        f"Preorder: {''.join(text for text in listChar if text not in ['(', ')'])}")
