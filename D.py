from sys import stdin

tablero = [[0 for k in range(8)] for k in range(8)]
movimientos = [[2, 1], [2, -1], [1, 2], [1, -2],
               [-1, 2], [-1, -2], [-2, 1], [-2, -1]]


def backtraking(tablero, casilla_actual, contador):
    for movimiento in movimientos:
        mov_x = casilla_actual[0] + movimiento[0]
        mov_y = casilla_actual[1]+movimiento[1]
        try:
            if mov_x >= 0 and mov_y >= 0 and tablero[mov_x][mov_y] == 0:
                tablero[mov_x][mov_y] = contador
                if contador == 64:
                    return tablero
                elif backtraking(tablero, [mov_x, mov_y], contador+1) is None:
                    tablero[mov_x][mov_y] = 0
                else:
                    return tablero
        except:
            continue
    return None


letters = [chr(a) for a in range(65, 73)]

# Leemos la casilla inicial
for input in stdin:
    posicion = input.rstrip("\n")
    break

# Traducimos el nombre de la casilla a la posicion en matriz
indice = [8-int(posicion[1]), letters.index(posicion[0])]
# Colocamos el primer valor en el tablero
tablero[indice[0]][indice[1]] = 1

# CALCULAMOS LOS RESULTADOS
resultado = backtraking(tablero, indice, 2)
if resultado is None:
    print("The Knight is trapped")
else:
    texto = ""
    for k in range(1, 65):
        for num_columna, filas in enumerate(resultado):
            if k in filas:
                texto += f"{letters[filas.index(k)]}{8-num_columna} "
                if k % 16 == 0:
                    print(texto[0:len(texto)-1])
                    texto = ""
