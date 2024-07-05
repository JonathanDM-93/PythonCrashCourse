from datetime import datetime
import math


class MasterDate:

    def __init__(self, Mater_date):
        self.Master_date = Mater_date

    def masterFormat(self):
        """Asignar el formato correcto a la fecha maestra para el resto de los calculos"""
        # Convertir la cadena de fecha a objeto datetime
        master_date = datetime.strptime(self.Master_date, '%Y-%m-%d')
        return master_date

    def piBimDates(self):
        """Determina a qué bimestre corresponde la fecha maestra y devuelve la fecha del mes que inicia el bimestre"""

        master_date = self.masterFormat()  # Toma la salida del método masterFormat
        # Calcular el bimestre
        bimester = math.ceil(master_date.month / 2)
        # Calcular el mes que inicia el bimestre
        start_month = (bimester - 1) * 2 + 1
        # Construir la fecha del mes que inicia el bimestre
        start_date = datetime(master_date.year, start_month, 1)
        # Formatear la fecha a string
        start_date_str = start_date.strftime('%Y-%m-%d')
        return start_date_str
