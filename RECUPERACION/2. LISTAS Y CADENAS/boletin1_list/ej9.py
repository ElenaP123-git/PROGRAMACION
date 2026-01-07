lista_num = []
for x in range(15):
    num = int(input("Dime un número: "))
    lista_num.append(num)

último = lista_num[-1]
lista_num.pop(-1)
lista_num.insert(0,último)
print(lista_num)