# Igualdad de sumas
matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def sumaPorFilasIgual(matriz):
    suma0 = sum(matriz[0])
    for fila in matriz:
        if sum(fila) != suma0:
            return False
    return True


def sumaColumna(matriz, columna):
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][columna]
    return total

def sumaPorColumnasIgual(matriz):
    columnas = len(matriz[0])
    suma0 = sumaColumna(matriz, 0)
    for j in range(columnas):
        if sumaColumna(matriz, j) != suma0:
            return False
    return True


def sumaTotalIgual(matriz):
    return sumaPorFilasIgual(matriz) and sumaPorColumnasIgual(matriz)

print(sumaPorFilasIgual(matriz))   # → True
print(sumaPorColumnasIgual(matriz))   # → True
print(sumaTotalIgual(matriz))   # → True
