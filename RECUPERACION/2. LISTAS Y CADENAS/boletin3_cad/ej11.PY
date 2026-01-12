# NÚMEROS NATURALES GRANDES (10.000.000)

cadena = input("Introduce un número grande (ej:28397424): ")

cad_rev = ""
for x in range (len(cadena)-1,-1,-1):
    cad_rev += cadena[x]

resultado = ""
contador = 0
for c in cad_rev:
    resultado += c
    contador += 1
    
    if contador == 3:
        resultado += "."
        contador = 0
if resultado[-1] == ".":
    resultado = resultado[:-1]

final = ""
for i in range(len(resultado)-1, -1, -1): 
    final += resultado[i]

print(final)