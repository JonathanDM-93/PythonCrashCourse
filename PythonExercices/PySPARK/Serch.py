lista1 = sorted([2, 3, 1, 5, 7, 40])
lista2 = sorted([3, 3, 8, 5, 40, 2])

#ORDENADA lista1 = [1, 2, 3, 5, 7, 40]
#ORDENADA lista2 = [2, 3, 3, 5, 8, 40]


ElementosIn: list = []
ElementosNot :list = []

for indice, (item1, item2) in enumerate(zip(lista1, lista2)):
    if item1 == item2:
        ElementosIn.append(item1)
        print(f"{item1} se encuentra en ambas listas en el índice {indice}")

    if item1 != item2:
        ElementosNot.append(item1)
        print(f"{item1} no encuentra en ambas listas en el índice {indice}")


print("En ambas listas:" + str(ElementosIn))
print("En una sola lista: " + str(ElementosNot))



