# Este es un nuevo ejemplo basado en el programa parrot.py
# Es este caso ahora emplearemos algo llamado flags que actua como una señal dentro
# de un programa.
# Utilizaremos las dos lineas iniciales de parrot.py

prompt: str = "\nPresiona 'quit' para terminar el programa."
prompt += '\nDime algo y te lo repetire: '

activeFlag: bool = True
message: str = ""
while activeFlag:  # Mientras la condición es TRUE
    message = input(prompt) # La variable message recibirá lo que el usuario ingreso

    if message == 'quit': # Si la palabra es 'quit' la bandera ahora será FALSA y se termina el programa
        activeFlag: bool = False
    else:
        print(message) # Si la activeFlag sigue siendo TRUE se imprime el mensaje.
