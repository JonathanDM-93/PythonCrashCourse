# TRY IT YOURSELF pág. 71
# Ya abordamos como ir trabajando con listas en los ejercicios anteriores en esta ocasión veremos como crear listas
# que no pueden cambiar o son inmutables, a este tipo de listas se les llama TUPLAS
# Una tupla a diferencia de una lista se define a traves de parentesis () y no corchetes [].
# Defina una tupla tambien podras acceder a cada eleemnto dentre de la misma a traves de su indice.

miTupla: tuple = (100, 10)
print(miTupla[0])
print(miTupla[1])
# 100
# 10
# Vemos que los que imprime es el valor que se guarda en el indice dentro de la tupla
# Ahora bien si nosotros qusieramos cambiar el valor dentro de la tupla podiramos hacer lo siguiente

print('\n[*]\n')

print('Tupla original: ' + str(miTupla))
miTupla: tuple = (30, 10)
print('Cambio de valores: ' + str(miTupla))
# En resumen sobreescribimos los valores en la variable anterior.
