from sys import stdin, stdout

# Creamos el tablero de juego
board = [[0 for k in range(8)] for k in range(8)]
# Creamos una lista con las letras de las columnas y el ascii
letters = [chr(a) for a in range(72, 64, -1)]

# Leemos la casilla inicial
for input in stdin:
    posicion = input.rstrip("\n")
    break

# Traducimos el nombre de la casilla a la posicion en matriz
indice = [letters.index(posicion[0]), int(posicion[1])-1]
# Colocamos el primer valor en el tablero
board[indice[0]][indice[1]] = 1


# Valida si hay posiciones por llenar
def validar_espacios(matriz):
    for fila in matriz:
        if 0 in fila:
            return False
    return True


# Funcion que hace el recorrido recursivo por backtraking
def recorrido(chess_board: list[list[int]], casilla_actual: list[int], contador: int):
    # Creamos una matriz con todos los movimientos posibles del caballero
    movimientos = [[1, 2], [-1, 2], [-1, -2],
                   [1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

    # Ciclo que recorre los movimientos posibles
    for movimiento in movimientos:
        mov_x = casilla_actual[0]+movimiento[0]
        mov_y = casilla_actual[1]+movimiento[1]
        try:
            if chess_board[mov_x][mov_y] == 0 and mov_x >= 0 and mov_y >= 0:
                # Si la suma de los indices son positivas y la casilla esta libre actualizamos
                chess_board[mov_x][mov_y] = contador
                # Nos intentamos mover con una nueva llamada a la funcion con el tablero actualizado
                recorrido(chess_board, [mov_x, mov_y], contador+1)
                # Si termina el nuevo recorrido sin ningun cambio fue porque no habian nuevos movimientos
                # Cambiamos el valor a 0 para seguir buscando posibilidades
                chess_board[mov_x][mov_y] = 0
        except:
            pass
    # Si termina el ciclo que es que ha probado todos los movimientos posibles para la casilla actual
    # Como ya los probo todos verificamos si quedan espacios en blanco, en caso de que no queden retornamos el tablero
    # Si quedan movimientos sale de la funcion y va al movimiento anterior
    if validar_espacios(chess_board):
        return chess_board
    if contador >= 62:
        print(contador)


print(recorrido(board, indice, 2))
