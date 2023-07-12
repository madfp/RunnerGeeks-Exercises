from sys import stdin, stdout


# DEFINIMOS LAS FUNCIONES PRINCIPALES
# Funcion que calcula el peso de los movimientos posiles del caballo y los devuelve el orden en que se deben hacer
def calcular_pesos(chess_board: list[list[int]], casilla_actual: list[int]):
    # Creamos una matriz con todos los movimientos posibles del caballero
    movimientos = [[2, 1], [2, -1], [1, 2], [1, -2],
                   [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
    pesos = []
    movimientos_finales = []

    for movimiento in movimientos:
        cont = 1
        mov_x = casilla_actual[0]+movimiento[0]
        mov_y = casilla_actual[1]+movimiento[1]
        # Si el movimiento sale del tablero su peso es 0
        # En caso contrario se procede a calcular su peso
        if mov_x not in range(0, 8) or mov_y not in range(0, 8):
            pesos.append(0)
        else:
            actual = [mov_x, mov_y]
            # Los movimientos pasan a ser los valores actuales para la evaluacion
            # Creamos la nueva iteracion para calcular los pesos
            for nuevo_movimiento in movimientos:
                new_mov_x = actual[0] + nuevo_movimiento[0]
                new_mov_y = actual[1] + nuevo_movimiento[1]
                if new_mov_x in range(0, 8) and new_mov_y in range(0, 8) and chess_board[new_mov_x][new_mov_y] == 0:
                    cont += 1
            pesos.append(cont)

    for k in range(1, 8):
        for j in range(len(pesos)):
            if pesos[j] == k:
                movimientos_finales.append(movimientos[j])
    return movimientos_finales


# Funcion que hace el recorrido recursivo por backtraking
def recorrido(chess_board: list[list[int]], casilla_actual: list[int], contador: int):
    # Obtenemos ls mejores movimientos posibles para el caballo en orden
    movimientos = calcular_pesos(chess_board, casilla_actual)
    # Ciclo que recorre los movimientos posibles
    for movimiento in movimientos:
        mov_x = casilla_actual[0]+movimiento[0]
        mov_y = casilla_actual[1]+movimiento[1]

        if chess_board[mov_x][mov_y] == 0 and mov_x >= 0 and mov_y >= 0:
            # Si la suma de los indices son positivas y la casilla esta libre actualizamos
            chess_board[mov_x][mov_y] = contador
            if contador == 64:
                return chess_board
            else:
                # Nos intentamos mover con una nueva llamada a la funcion con el tablero actualizado
                return recorrido(chess_board, [mov_x, mov_y], contador+1)


# Creamos el tablero de juego
board = [[0 for k in range(8)] for k in range(8)]
# Creamos una lista con las letras de las columnas y el ascii
letters = [chr(a) for a in range(65, 73)]

# Leemos la casilla inicial
for input in stdin:
    posicion = input.rstrip("\n")
    break

# Traducimos el nombre de la casilla a la posicion en matriz
indice = [8-int(posicion[1]), letters.index(posicion[0])]
# Colocamos el primer valor en el tablero
board[indice[0]][indice[1]] = 1

# CALCULAMOS LOS RESULTADOS
resultado = recorrido(board, indice, 2)
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
