import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta


def ultimo_dia_siguiente_mes(master_date):
    """
    Calculate the last day of the month following the given master date.
    :param master_date: A string representing the master date in the format 'YYYY-MM-DD'.
    :return:
    str: A string representing the last day of the month following the given master date in the format 'YYYY-MM-DD'.
    """
    # Convertir la cadena de fecha a objeto datetime
    master_date = datetime.strptime(master_date, '%Y-%m-%d')

    # Determinar el mes siguiente
    mes_siguiente = master_date.month + 1

    ano_siguiente = master_date.year + (mes_siguiente // 13)
    mes_siguiente %= 12
    if mes_siguiente == 0:
        mes_siguiente = 12

    # Obtener el último día del mes siguiente
    ultimo_dia = calendar.monthrange(ano_siguiente, mes_siguiente)[1]

    # Formatear la salida
    output = datetime(ano_siguiente, mes_siguiente, ultimo_dia).strftime("%Y-%m-%d")

    return output


# ------------------------------------------------------------------------------------------------------------------- #

def calcular12_Mes_Atras(master_date):
    """
    Calculate the date 12 months ago from the given master date.
    :param master_date: A string representing the master date in the format 'YYYY-MM-DD'.
    :return:
    str: A string representing the date 12 months ago from the given master date in the format 'YYYY-MM-DD'.
    """
    # Convertir la cadena de fecha a objeto datetime
    master_date = datetime.strptime(master_date, '%Y-%m-%d')
    # Calcular 12 meses atrás
    fecha_ano_atras = master_date - relativedelta(months=12)

    return fecha_ano_atras.strftime("%Y-%m-%d")


# -------------------------------------------------------------------------------------------------------------------- #

def get_bloque(master_date):
    """

    :param master_date: A string representing the master date in the format 'YYYY-MM-DD'.
    :return:
    """
    next_mont_master_date = ultimo_dia_siguiente_mes(master_date)  # <class 'str'>

    pastYear_master_date = calcular12_Mes_Atras(master_date)

    pastYear_next_mont_master_date = calcular12_Mes_Atras(next_mont_master_date)

    return [master_date, next_mont_master_date, pastYear_master_date, pastYear_next_mont_master_date]


# ---------------------------------------Llamada de la función get_bloque ------------------------------------------- #

# Ejemplo de uso Asignar el mes inicial del bimestre a calcular
master_date = '2024-01-01'

bloque_fechas_1 = get_bloque(master_date)
print(bloque_fechas_1)  # ['2024-01-01', '2024-02-29', '2023-01-01', '2023-02-28']

# Convertir a un formato válido para el manejo de fechas
master_date = datetime.strptime(master_date, '%Y-%m-%d')

# Restar dos meses a master_date
masterDate_BackTwoMonths = master_date - relativedelta(months=2)

# Convertir a un formato string el resultado de la resta de dos meses
masterDate_BackTwoMonths = masterDate_BackTwoMonths.strftime("%Y-%m-%d")

print(f"Restar dos meses a master_date: {masterDate_BackTwoMonths}")

bloque_fechas_2 = get_bloque(masterDate_BackTwoMonths)
print(bloque_fechas_2)
