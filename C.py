from sys import stdin, stdout


class node:
    def __init__(self, value) -> None:
        self.value = value
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None

    def get_value(self):
        return self.value


class quad_tree:
    def __init__(self, matriz: list[list], treshold: int) -> None:
        self.root = node(matriz)
        self.treshold = treshold

    def evaluar_separacion(self):
        raiz = self.root.get_value()
        if len(raiz) == 1:
            return raiz[0][0]
        else:
            average = sum([sum(filas) for filas in raiz]) / len(raiz)
            error = sum([abs(valor - average)
                        for fila in raiz for valor in fila])

            if error <= self.treshold:
                return 1
            else:
                return "No se que hacer"

    def separar_matriz(self):
        pass


matriz = []
# Leemos la entrada
for k, inputs in enumerate(stdin):
    if k == 0:
        listaValores = inputs.rstrip("\n").split(" ")
        size, t = int(listaValores[0]), int(listaValores[1])
    else:
        if k <= size:
            matriz.append([int(valores)
                          for valores in inputs.rstrip("\n").split(" ")])
            if k == size:
                break

arbol = quad_tree(matriz, t)
print(arbol.evaluar_separacion())
