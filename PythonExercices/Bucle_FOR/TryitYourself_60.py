# TRY IT YOURSELF pag 60
# En esta sección trabajaremos con las listas y como pasar a traves de casa elemento.
# Vamos a usar una lista que anteriormente ocupamos:

ToyotaList: list = ['Yaris', 'Corolla', 'Camry', 'Tundra', 'Avanza']

# Cuando requerimos que una accicón de ejecute en cada elemento de una lista podemos utilizar un for
# En este caso solo queremos que se imprima un elemento a la vez:

for models in ToyotaList:
    print(models)

# Como observamos cada modelo se imprimio uno a la vez
# Yaris
# Corolla
# Camry
# Tundra
# Avanza

# Aqui observamos de forma simple como genererar un loop
# Para reforzar lo aprendido reproduszcamos un ejemplo del libro

magos: list = ['Jonathan', 'Katia', 'Francisco']
for names in magos:
    print(names + ' eso fue un excelente truco!')
    print('No puedo esperar por el ver el siguiente, ' + names + '.\n')




