# Suma de una columna (columna → suma)

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def sumaColumna(matriz, columna):
    total = 0
    for i in range(len(matriz)):
        total += matriz[i][columna]
    return total

print(sumaColumna(matriz, 0))   # columna 0 → 8 + 3 + 4 = 15
