# Comienza con una lista de usuarios que quieres confirmar
unconfirmed_users: list = ['Jonathan', 'Moises', 'Sigrid']

# Lista vaciá para almacenar a los usuarios
confirmed_users: list = []

# Funciona como in while que esta recorriendo cada elemento en la lista.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verificando usuario : {current_user}")
    confirmed_users.append(current_user)
    confirmed_users.sort()

# Imprime a todos los usuarios confirmados uno a uno
print("\nLos siguientes usuarios fueron confirmados:")

for i in confirmed_users:
    print(i)



