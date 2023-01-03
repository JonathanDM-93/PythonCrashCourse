# Una lista en un Diccionario
# Ahora es momento de explorar la forma que podemos almacenar una lista dentro de un diccionario
# y aprovechar las ventajas que esto nos puede ofrecer

# El ejemplo del libro relata que supongamos que una persona pide una pizza y claramente estas
# pueden tener diferentes coberturas. Con un diccionario una lista de coberturas puede solo ser
# un solo aspecto de la pizza que estas describiendo.
# En el sig. Ejemplo guardaremos dos tipos de informacion: tipo de corteza y una lista de cober-
# turas.

# Guaremos la informacion de la pizza que estamos por ordenar

pizza: dict = {
    'corteza': 'delgada',
    'cobertura': ['Champiñones', 'Piña'],
}

# Llamo al nombre del diccionario accedo a la LLAVE para imprimir el valor
print('La pizza que ordenaste tiene la corteza: ' + pizza['corteza'] + ' con las siguientes coberturas: ')
for item in pizza['cobertura']:
    print(item)


