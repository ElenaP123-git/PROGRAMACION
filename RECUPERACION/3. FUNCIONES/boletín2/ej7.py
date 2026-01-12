# Suma de filas pares (filas 0, 2, 4… → suma)

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def sumaFilasPares(matriz):
    total = 0
    for i in range(len(matriz)):
        if i % 2 == 0:
            total += sum(matriz[i])
    return total

print(sumaFilasPares(matriz))   # filas 0 y 2 → (8+1+6) + (4+9+2)
