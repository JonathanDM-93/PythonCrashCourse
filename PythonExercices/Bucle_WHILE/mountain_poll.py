# Ingresando valores a un diccionario
# Crear una variable de in diccionario vació
responses : dict = {}

# Agrega una bandera
polling_active : bool = True

while polling_active:
    # Pregunta al usuario su nombre
    name: str = input ('¿Cuál es tu nombre? ')
    response : str = input ('¿Qué montaña deseas escalar hoy? ')

    # Guarda la respuesta en el diccionario
    responses[name] = response

    # Averigua si alguien mas quiere agregarse a la lista
    repeat : str = input('¿Deseas agregar otra persona? (yes/no) ')
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print ("\n --- Resultados ---")
for name, response in responses.items():
    print(name + " la montaña que deseas escalar es " + response)

# --- Resultados ---
# Jonathan la montaña que deseas escalar es Orizaba
# Juan la montaña que deseas escalar es Perote





