# Usando la declaración CONTINUE en un loop while
StartNum: int = 0

while StartNum < 10: # Mientras el StartNum sea menor o igual a 10 se mantiene la condición TRUE
    StartNum += 1 # Aumenta en 1 cada vez que se ingresa en el loop
    if StartNum % 2 == 0: # Si el StartNum es divisible entre 2 y su residuo es 0
        continue
    print(StartNum) # Se imprime los valores que devuelven residuo

# >>
# 1
# 3
# 5
# 7
# 9

# La declaración continue le dice a python que ignore el resto del loop y retorne al principio. Si el número
# no es divisible por 2 el resto del loop es ejecutado y python lo imprime.