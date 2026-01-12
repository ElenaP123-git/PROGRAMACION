# Obtener columna completa columna → lista)

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def obtenerColumna(matriz, columna):
    col = []
    for i in range(len(matriz)):
        col.append(matriz[i][columna])
    return col

print(obtenerColumna(matriz, 1))   # → [1, 5, 9]
