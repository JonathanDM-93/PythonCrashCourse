# TRY IT YOURSELF pag 33 List
# Una lista simplemente es una coleccion de objetos en un orden particular
# Su estructura es la siguiente:
# 3.1 Guarda los nombres de algunas personas en una lista.
names: list = ['Jonathan', 'Vicente', 'Joselyne', 'Eduardo']
# Imprimir lista
for item in names:
    print('Nombres: ' + item)

print('\n')

# 3.2 Usa la lista anterior y agrega un mensaje personalizado para cada elemento en la lista
text1: str = "Este es mi nombre: "
text2: str = "Compañero de trabajo: "
text3: str = "Mi amiga: "
text4: str = "Mi tio: "
MessagesList: list = [text1, text2, text3, text4]

# En este caso quería sumar las dos listas para que salieran tanto los nombres como los mensajes
emptyList: list = []
for i in range(len(names)):
    emptyList.append(MessagesList[i] + names[i])
    print(emptyList)

