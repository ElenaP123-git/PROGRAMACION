# Obtener fila completa (fila → lista)

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def obtenerFila(matriz, fila): 
    return matriz[fila] # for i in matriz: print(i)

print(obtenerFila(matriz, 0))   # → [8, 1, 6]

