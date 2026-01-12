# Suma de una fila (fila → suma)

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def sumaFila(matriz, fila):
    return sum(matriz[fila])

print(sumaFila(matriz, 2))   # fila 2 → 4 + 9 + 2 = 15
