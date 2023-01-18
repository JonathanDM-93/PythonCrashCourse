# El uso que podemos aplicar en los bucles while podría ser par determinar cuando queremos
# dar por terminado algún programa
# El siguiente ejemplo demuestra que hasta que se ingrese cierto valor dara por terminado el
# programa.
prompt: str = "\nPresiona 'quit' para terminar el programa."
prompt += '\nDime algo y te lo repetire: '

message: str = ""
while message != 'quit':
    message = input(prompt)
    print('\t' + 'ROBOT: ' + message)

