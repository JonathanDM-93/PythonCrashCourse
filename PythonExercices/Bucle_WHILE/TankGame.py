# Juego de tanques
# Si el usuario adivina el número aleatorio se destruye el tanque
import random

shotUser: str = 'Ingresa un número entre el 1 - 3: '
HPTank: int = 100
Shotrand: int = random.randint(1,3)
messageShot: str = ""
while HPTank != 0:
    messageShot = int(input(shotUser))
    if messageShot == Shotrand:
        HPTank = HPTank - 100
        print('Tanque destruido.')

