# Usando loop While con listas [] y diccionarios {}
# Hasta ahora solo hemos trabajado con una entrada de información a través de un usuario.
# Ahora a través del loop while recibiremos más entradas y responder. Pero para llevar
# un control de cuantos usuarios y piezas de información, necesitaremos hacer uso tanto de #
# las listas [] como los diccionarios {}
# USANDO LOOPS WHILE CON LISTAS Y DICCIONARIOS NOS PERMITIRÁ RECOLECTAR, ALMACENAR Y ORGANIZAR
# VARIAS ENTRADAS A EXAMINAR Y REPORTAR POSTERIORMENTE.

# Moviendo una lista a otra
# Considera que tienes nuevos usuarios registrados, pero que no han sido verificados.
# Después de ser revisados, ¿cómo los mueves de una lista de no confirmados a confirmados?

# 1. Crea un lista con nombres que deberán ser confirmados.
UnconfirmedUsers: list = ['tom', 'natalia', 'nicolas']
ConfirmedUsers: list = []

# 2. Verificar que cada usuario hasta que no haya más usuarios sin confirmar
# Mover a cada usuario en la lista de ConfirmedUsers
while UnconfirmedUsers: # El loop continuará hasta que la lista este vaciá
    currentUser: str = UnconfirmedUsers.pop() # Quitar a cada usuario de la lista UnconfirmedUsers

    print('Verificando a los usuarios: ' + currentUser.title())
    ConfirmedUsers.append(currentUser) # Agregar a la lista ConfirmedUsers los usuarios

# Imprimir a los usuarios confirmados
print('\nLos siguientes usuarios han sido confirmados con exito: ')
for user in ConfirmedUsers:
    var_user = user # Guardar cada valor en una variable para que después se use .title()
    print(var_user.title())

# >>
# Verificando a los usuarios: Nicolas
# Verificando a los usuarios: Natalia
# Verificando a los usuarios: Tom
#
# Los siguientes usuarios han sido confirmados con exito:
# Nicolas
# Natalia
# Tom


