import re
from datetime import datetime


def datesBetween(enter_list):
    result_list = []
    regex = r"^\d{4}-\d{2}-\d{2}$"
    for i in enter_list:
        if re.match(regex, i) is None:
            print(f"{i}, no cumple el regex")
        else:
            result_list.append(i)

    return result_list[0], result_list[-1]


fecha_list = ['2023-08-01', '2023-09-01', '2023-10-01']
guardar = datesBetween(fecha_list)


#print(guardar)
#print(type(guardar))


def is_date_in_range(list_path_content, inicio_rango, fin_rango):
    """
    Verifica si una fecha está dentro de un rango de fechas dado.
    Args:
        fecha_str (str): La fecha que se desea verificar en formato de cadena.
        inicio_rango_str (str): La fecha de inicio del rango en formato de cadena.
        fin_rango_str (str): La fecha de fin del rango en formato de cadena.
    Returns:
        bool: True si la fecha está dentro del rango, False de lo contrario.
    """
    regex = r"^\d{4}-\d{2}-\d{2}$"

    if re.match(regex, list_path_content) is None:
        # print(f"{fecha_str}, no cumple el regex")
        return False

    fecha = datetime.strptime(list_path_content, '%Y-%m-%d').date()
    inicio_rango = datetime.strptime(inicio_rango, '%Y-%m-%d').date()
    fin_rango = datetime.strptime(fin_rango, '%Y-%m-%d').date()

    # print(f"fecha: {fecha}")
    return inicio_rango <= fecha <= fin_rango


path_content: list = ['_SUCCESS',
                      'cutoff_date=2023-01-01',
                      'cutoff_date=2024-03-01',
                      'cutoff_date=2024-01-01',
                      'cutoff_date=2024-04-01',
                      'cutoff_date=2023-08-01',
                      'cutoff_date=2022-10-01',
                      'cutoff_date=2024-05-01',
                      'cutoff_date=2023-05-01',
                      '_not_overwritten',
                      'cutoff_date=2023-02-01',
                      'cutoff_date=2022-08-01',
                      'cutoff_date=2022-12-01',
                      'cutoff_date=2023-04-01',
                      'cutoff_date=2023-12-01',
                      'cutoff_date=2023-09-01',
                      'cutoff_date=2023-03-01',
                      'cutoff_date=2022-09-01',
                      'cutoff_date=2023-10-01',
                      'cutoff_date=2023-11-01',
                      'cutoff_date=2022-07-01',
                      'cutoff_date=2023-07-01',
                      'cutoff_date=2024-02-01',
                      'cutoff_date=2022-11-01']

oneDate = "2023-06-01"

dates_checkRegex = []
regex = r"^\d{4}-\d{2}-\d{2}$"

for path_i in path_content:
    # Primero se quedan con las fechas de la lista
    date_str_i = path_i.split('/')[-1].split('=')[-1]

    if re.match(regex, date_str_i) is None:
        """print(f"{date_str_i}, no cumple el regex")"""
    else:
        # Si cumple el regex, se almacenara en la lista
        dates_checkRegex.append(date_str_i)

#-------------------------------------------------------------------------------------------------------#

# Convertir la fecha objetivo a un objeto datetime
MASTER_DATE = datetime.strptime(oneDate, '%Y-%m-%d').date()

# Inicializar la variable para la fecha resultante
closest_previous_date = None

# Encontrar la fecha más cercana anterior a oneDate si oneDate no está en la lista
if oneDate not in dates_checkRegex:
    for date_str in dates_checkRegex:
        #Itera en la lista de fechas y les cambia el formato
        date_dt = datetime.strptime(date_str, '%Y-%m-%d').date()
        if date_dt < MASTER_DATE:
            if closest_previous_date is None or date_dt > closest_previous_date:
                closest_previous_date = date_dt


print(closest_previous_date)