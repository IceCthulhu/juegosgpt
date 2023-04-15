altura = int(input("Ingrese la altura del árbol: "))
simbolo = input("Ingrese el símbolo para el árbol: ")

# Imprimir la estrella
for i in range(altura):
    print(" ", end="")
if altura % 2 == 0:
    print("*")
else:
    print("*")

# Imprimir el cuerpo del árbol
for i in range(altura):
    for j in range(altura-i):
        print(" ", end="")
    for k in range(2*i+1):
        print(simbolo, end="")
    print()

# Imprimir el tronco del árbol
for i in range(3):
    for j in range(altura-3):
        print(" ", end="")
    print(simbolo*7)


