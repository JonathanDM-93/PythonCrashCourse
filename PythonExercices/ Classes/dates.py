from datetime import datetime
from dateutil.relativedelta import relativedelta

def restar_meses(fecha, meses_a_restar):
    # Convertir la cadena de fecha en un objeto datetime
    fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')

    # Restar meses utilizando relativedelta
    nueva_fecha = fecha_obj - relativedelta(months=meses_a_restar)
    nueva_fecha = nueva_fecha.strftime('%Y-%m-%d')

    return nueva_fecha

# Ejemplo de uso
fecha = '2024-04-10'
meses_a_restar = 12
nueva_fecha = restar_meses(fecha, meses_a_restar)
print(nueva_fecha)
"""
print("Fecha original:", fecha)
print("Nueva fecha después de restar", meses_a_restar, "meses:", nueva_fecha.strftime('%Y-%m-%d'))
"""