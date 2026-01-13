# Diagonales de la matriz

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def diagonalPrincipal(matriz):
    diag = []
    for i in range(len(matriz)):
        diag.append(matriz[i][i]) # fila 0, col 0, fila 1, col 1...
    return diag

def diagonalSecundaria(matriz):
    diag = []
    n = len(matriz)
    for i in range(n):
        diag.append(matriz[i][n - 1 - i])
    return diag

print(diagonalPrincipal(matriz))   # → [8, 5, 2]
print(diagonalSecundaria(matriz))  # → [6, 5, 4]
