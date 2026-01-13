# Suma total de la matriz (sumatorio de todos los elementos)
# siempre que hay que recorrer la matríz, se necesitan 2 for

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

def sumaMatriz(matriz): 
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

print(sumaMatriz(matriz))   # → 45
