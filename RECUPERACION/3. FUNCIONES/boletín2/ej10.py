# Máximos en la matriz

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def maxFila(matriz, fila):
    return max(matriz[fila])

def maxColumna(matriz, columna):
    maximo = matriz[0][columna]
    for i in range(len(matriz)):
        if matriz[i][columna] > maximo:
            maximo = matriz[i][columna]
    return maximo

def maxTotal(matriz):
    maximo = maxFila(matriz, 0)   # empezamos con la fila 0
    for i in range(len(matriz)):
        valorFila = maxFila(matriz, i)
        if valorFila > maximo:
            maximo = valorFila
    return maximo

print(maxFila(matriz, 1))   # → 7
print(maxColumna(matriz, 2))   # → 7
print(maxTotal(matriz))   # → 9
