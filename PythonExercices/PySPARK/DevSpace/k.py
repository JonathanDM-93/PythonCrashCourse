# Se compara la segunda lista con la primera
# Se debe ordenar
lst =     [1,2,3,5,6]
lsttest = [1,2,3,5,6,7,8,9]
NO = []
SI = []


for i in lsttest:
    if not i in lst:
        print("No esta en lst:"+ str(i))
        NO.append(i)
    else:
        print("Si esta:" + str(i))
        SI.append(i)

# Con string para saber si algún elemento no se encuentra en otro pero deben estar ordenados
ListStringOne : list = ['hola', 'adios']
ListStringTwo: list = ['Hola', 'Adios', 'item_extra']

# Lo conveniente sería aplicar un sort para ordenar y aplicar la similitud
ListStringOne.sort()
ListStringTwo.sort()

# Pone en minúsculas los elementos de la lista
for i in range(len(ListStringTwo)):
    ListStringTwo[i] = ListStringTwo[i].lower()
print(ListStringTwo)

# Este for ayuda a saber si existen similitudes entre listas
for i in ListStringTwo:
    if not i in ListStringOne:
        print("No esta en lst:"+ str(i))
        NO.append(i)
    else:
        print("Si esta:" + str(i))
        SI.append(i)

