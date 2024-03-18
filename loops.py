array = [1, 2, 3, 4]

# Permite tener el indice como el valor del arreglo
enum = enumerate(array)
# Loop for in


def enumerar(a):
    for indice, valor in enumerate(a):
        print(f"Indice: {indice}, Valor: {valor}")


def print_array_with_for(a):
    for i in range(len(a)):
        print(a[i])


def print_array_with_while(a):
    i = 0
    while i < len(a):
        print(a[i])
        i += 1


enumerar(array)
