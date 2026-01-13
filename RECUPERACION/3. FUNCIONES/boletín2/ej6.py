# Suma de una fila (fila → suma)

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def sumaFila(matriz, fila):
    suma = 0
    for elemento in matriz[fila]:
        suma = suma + elemento
    return suma

print(sumaFila(matriz, 2))   # fila 2 → 4 + 9 + 2 = 15
