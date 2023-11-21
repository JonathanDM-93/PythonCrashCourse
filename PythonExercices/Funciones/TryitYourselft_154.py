# TRY IT YOURSELF pag. 154 8-12 Sandwiches
# Escribe una función que acepte una lista de elementos de personas que quieren un sandwich. La función debe tener un
# parametro que recolecte todos los elementos que se ingresen y debe imprimir el resumen de los sanwiches que se
# ordenaron.

def make_sandwich(person_name, *ingredientes):
    print(f"El cliente: {person_name.upper()} quiere un sandwich con los siguientes ingredientes: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


make_sandwich('Jonathan', 'Jamon', 'Jitomante', 'Lechuga', 'Queso')
# El cliente: JONATHAN quiere un sandwich con los siguientes ingredientes:
# - Jamon
# - Jitomante
# - Lechuga
# - Queso

print("\n[*]\n")

