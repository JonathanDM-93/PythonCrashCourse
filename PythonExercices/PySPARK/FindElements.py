#index = [0, 1, 2, 3, 4]
lista1 = [2, 3, 1, 5, 7]
lista2 = [3, 3, 8, 5, 0]

ElementosIn: list = []
ElementosNot :list =[]

longitud = len(lista1) # Longitud 6 elementos en este ejemplo
indice_lista1 = 0
indice_lista2 = 0
while indice_lista1 < longitud:
    item = lista1[indice_lista1]
    item2 = lista2[indice_lista2]

    if item == lista2[indice_lista1]:
        print(f"El elemento {item} se encuentra en ambas listas")
        ElementosIn.append(item)
    indice_lista1 += 1

    if item2 != lista1[indice_lista2]:
        print(f"El elemento {item2} no encuentra en ambas listas")
        ElementosNot.append(item2)
    indice_lista2 += 1




print(ElementosIn)
print(ElementosNot)