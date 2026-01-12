# Suma de una diagonal

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def esCuadrada(matriz):
    return len(matriz) == len(matriz[0])

def diagonalPrincipal(matriz):
    diag = []
    for i in range(len(matriz)):
        diag.append(matriz[i][i])
    return diag

def diagonalSecundaria(matriz):
    diag = []
    n = len(matriz)
    for i in range(n):
        diag.append(matriz[i][n - 1 - i])
    return diag

def sumaDiagonal(matriz, esPrincipal):
    if not esCuadrada(matriz):
        return 0
    if esPrincipal:
        return sum(diagonalPrincipal(matriz))
    else:
        return sum(diagonalSecundaria(matriz))

print(sumaDiagonal(matriz, True))   # → 8 + 5 + 2 = 15
print(sumaDiagonal(matriz, False))  # → 6 + 5 + 4 = 15
