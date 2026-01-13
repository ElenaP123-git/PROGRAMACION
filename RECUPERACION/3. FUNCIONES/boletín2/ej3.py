# Obtener columna completa columna → lista)

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def obtenerColumna(matriz, columna):
    col = []
    for i in range(len(matriz)):
        col.append(matriz[i][columna]) # fila 0,1 o 2 --> elemento columna (0,1,2) en fila
    return col                         # elemento en fila 0,1 o 2 == columna

print(obtenerColumna(matriz, 1))   # → [1, 5, 9]
