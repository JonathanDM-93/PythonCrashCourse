# Retomemos un ejemplo que desarrollamos anteriormente modificándolo un poco
# para ver como podemos acceder tanto a las llaves y los valores asociados a ellas a traves
# de algunos for.

lenguajes_favoritos: dict = {
    'Jonathan': ['Python', 'C++'],
    'Karen': ['Ruby'],
    'Arnold': ['JAVA', 'VisualStudio'],
    'Jenny': ['Pearl', 'Python', 'SQL'],
}

for nombre in lenguajes_favoritos.keys():
    print('\n' + '¡El lenguaje favorito de ' + nombre + ' es:')
    for lenguaje in lenguajes_favoritos[nombre]:
        print(lenguaje)

