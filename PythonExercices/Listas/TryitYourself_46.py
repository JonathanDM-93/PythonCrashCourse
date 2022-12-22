# TRY IT YOURSELF pag 46 List
# En esta sección abordaremos las formas de como modificar, agregar y remover elemento de una lista
# Crearemos una lista que contenga una serie de elementos como automoviles de la marca VW


VWList: list = ['Sentra', 'Virtus', 'Polo', 'Tiguan', 'Gol']

# Si qusieramos cambiar un elemento en particular, ubicamos que lugar ocupa dentro de la lista y cambiamos por el
# nuevo modelo de un auto, en este caso cambiaremos el modelo sentra ya que no pertenece a la marca VW sino a Nissan

VWList[0] = 'Vento'
print(VWList)
# ['Vento', 'Virtus', 'Polo', 'Tiguan', 'Gol']

# Ahora bien si queremos agregar un nuevo elemento a la lista que estamos utilizando VWList podemos utilizar el metodo
# .append()

VWList.append('Jetta')
print(VWList)
# ['Vento', 'Virtus', 'Polo', 'Tiguan', 'Gol', 'Jetta']
# Observamos que el nuevo elemento se agrega al final de la lista

# Ahora vamos a remover elemento de una lista
# Primero utilizaremos la declaración del, seguiremos utilizando la lista VW
# ['Vento', 'Virtus', 'Polo', 'Tiguan', 'Gol', 'Jetta']

del VWList[3]
print(VWList)
# Cuando se ejecuta la linea 27 vemos que se elimina el modelo 'Tiguan'
# ['Vento', 'Virtus', 'Polo', 'Gol', 'Jetta']
# Al usar la declaración del ya no podras acceder al elemento que se elimino

# Continuando con el topico de como eliminar elemento de una lista, ahora utilizaremos el método .pop()
# Con este método podemos usar nuevamente el elemento que se removio de una lista original VW
# ['Vento', 'Virtus', 'Polo', 'Gol', 'Jetta']

# En este caso utilizamos el método .pop() a la lista VWList y este elemento eliminado lo guardamos en una variable
# Observamos que podemos elegir el elemento dentro de la lista que queremos quitar
poppedList = VWList.pop(1)
print(poppedList)
# Virtus

# En resumen tanto la declaración del y el método .pop() remueven un elemento dentro de una lista la única diferencia
# es que del lo elimina y no puedes utilizar nuevamente el elemento al contrario que .pop()

# Ahora aprenderemos a remover un elemento a partir de su valor y crearemos otra lista
FordList: list = ['Escape', 'Ranger', 'F-150', 'Bronco']

# Utilizaremos el método .remove()
FordList.remove('F-150')
print(FordList)
# ['Escape', 'Ranger', 'Bronco']
# Podemos observar que se elimino directamente el modelo F-150

# Con el método .insert() podemos agregar nuvemanete el modelo de F-150 en la misma posición donde se encontraba
FordList.insert(2, 'F-150')
print(FordList)
# ['Escape', 'Ranger', 'F-150', 'Bronco']


