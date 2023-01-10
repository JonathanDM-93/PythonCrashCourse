# Algo que nos falto abordar son los llamados sets, algo interesate de este tipo de datos
# es que no se puede repetir sus valores dentro de ellos. Veamos algunos ejemplos y lo que
# se puede hacer con ellos.

# Este es un simple ejemplo de un set el cual puede almacenar cualquier tipo de dato, sin embargo,
# vemos que colocamos un valor repetido el cual ignora una vez que imprimimos.
my_Set: set = {'Hola', 12.43, False, 'Internet', 12.43}
# print(my_Set)
#  >> {False, 'Internet', 'Hola', 12.43}

# Para agregar un nuevo elemento al set usamos el método .add()
my_Set.add('Nuevo valor')
# print(my_Set)
#  >> {False, 'Internet', 12.43, 'Nuevo valor', 'Hola'}

# Para agregar más de un valor al SET podemos usar el metodo .update()
my_Set.update({'Agregar 1', 'Agregar 2', 'Agregar 3'})
# print(my_Set)
# >> {False, 'Agregar 1', 'Nuevo valor', 12.43, 'Agregar 2', 'Hola', 'Agregar 3', 'Internet'}

# Para remover algún elemento
my_Set.remove('Agregar 1')
# print(my_Set)
# >> {False, 'Hola', 'Internet', 'Agregar 3', 12.43, 'Agregar 2', 'Nuevo valor'}

# También podemos usar el método .discard() el cual busca y si no encuentra
# el elemento que deseamos eliminar no manda un mensaje de error, simplemente no
# hace nada.

my_Set.discard('Agregar 8')
# print(my_Set)
# Vemos que ese elemento no existe en el set asi que no sucede nada solo se imprime el set
# >> {False, 'Agregar 3', 'Hola', 'Internet', 'Agregar 2', 'Nuevo valor', 12.43}

# Eliminar todos los valores dentro del conjunto con el método .clear()

my_Set.clear()
# print(my_Set)
# >> set()
# Imprime un set vació.




