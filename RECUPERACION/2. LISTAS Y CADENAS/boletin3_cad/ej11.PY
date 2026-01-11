# NÚMEROS NATURALES GRANDES (10.000.000)

cadena = input("Introduce un número grande (ej:28397424): ")



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