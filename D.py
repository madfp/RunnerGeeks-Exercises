from sys import stdin

# Creamos el tablero en forma de matriz con todos los valores en 0
tablero = [[0 for k in range(8)] for k in range(8)]
# Creamos una lista de todos los movimientos posibles realizados por los caballos
movimientos = [[2, 1], [2, -1], [1, 2], [1, -2],
               [-1, 2], [-1, -2], [-2, 1], [-2, -1]]


# Funcion recursica que recibe como parametros
# tablero: Matriz con los movimientos realizados
# casilla_actual: Posicion actual del caballo en el tablero en 'x' e 'y'
# contador: Numero entero que representa la cantidad de movimientos del caballo en el tablero
def backtraking(tablero: list[list[int]], casilla_actual: list[int], contador: int) -> (list[list] | None):
    # Cada iteracion es un movimiento posible del caballo
    for movimiento in movimientos:
        # Calculamos cual deberia ser su siguiente movimiento
        mov_x = casilla_actual[0] + movimiento[0]
        mov_y = casilla_actual[1] + movimiento[1]
        # Verificamos si los movimientos estan dentro del tablero y que el espacio este vacio
        if mov_x in range(0, 8) and mov_y in range(0, 8) and tablero[mov_x][mov_y] == 0:
            # Actualizamos el tablero
            tablero[mov_x][mov_y] = contador
            # Si el contador llego a 64 significa que encontro un resultado por lo que retornamos el tablero
            if contador == 64:
                return tablero
            # En caso de que aun no sea 64 aplicamos el backtraking, si es None deshacemos el movimiento y continuamos
            elif backtraking(tablero, [mov_x, mov_y], contador+1) is None:
                tablero[mov_x][mov_y] = 0
            # En caso de que el backtraking no sea none es que encontro la solucion
            else:
                return tablero
    # Si se acabo el ciclo es que se ha acabado la rama de posibilidades por lo que retornamos None
    return None


letters = [chr(a) for a in range(65, 73)]

# Leemos la casilla inicial
for input in stdin:
    posicion = input.rstrip("\n")
    break

# Traducimos el nombre de la casilla a la posicion en matriz donde el numero es la fila y la letra la columna
indice = [8-int(posicion[1]), letters.index(posicion[0])]
# Colocamos el primer valor en el tablero
tablero[indice[0]][indice[1]] = 1

# CALCULAMOS LOS RESULTADOS
resultado = backtraking(tablero, indice, 2)

# Si no hay solucion posible mostramos el mensaje, en caso contrario imprimos la secuencia de movimientos
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
