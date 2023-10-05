# Toma el nombre y apellido y regresa el nombre comppleto formateado

def get_formatted_name(first_name, last_name):
    """Regresa el nombre completo"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musico = get_formatted_name("Jonathan", "Maldonado")
print(musico)
# Jonathan Maldonado
