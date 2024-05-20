from datetime import datetime

from dateutil.relativedelta import relativedelta


class MasterDate:

    def __init__(self, Mater_date):
        self.Master_date = Mater_date

    def masterFormat(self):
        """Asignar el formato correcto a la fecha maestra para el resto de los calculos"""
        # Convertir la cadena de fecha a objeto datetime
        master_date = datetime.strptime(self.Master_date, '%Y-%m-%d')
        return master_date

    def tla117_1(self):
        """Calcula tres fechas específicas a partir de master_date"""
        master_date = self.masterFormat()  # Toma la salida del método masterFormat
        # Calcular las fechas deseadas
        dates = [
            master_date,
            master_date - relativedelta(months=1),
            master_date - relativedelta(months=2)
        ]
        # Ordena las fechas
        dates.sort()
        # Regresa una lista con el formato
        return [date.strftime('%Y-%m-%d') for date in dates]

    def tla117_0(self):
        """Calcula tres fechas específicas a partir de master_date"""
        master_date = self.masterFormat()  # Toma la salida del método masterFormat
        # Calcular las fechas deseadas
        dates = [
            master_date - relativedelta(months=3),
            master_date - relativedelta(months=4),
            master_date - relativedelta(months=5)
        ]
        # Ordena las fechas
        dates.sort()
        # Regresa una lista con el formato
        return [date.strftime('%Y-%m-%d') for date in dates]


Ingresar_MasterDate = MasterDate("2023-10-01")
FechaCorrect = Ingresar_MasterDate.masterFormat()
print(FechaCorrect)

fechas_calculadas_tla117_1 = Ingresar_MasterDate.tla117_1()
print(fechas_calculadas_tla117_1)

fechas_calculadas_tla117_0 = Ingresar_MasterDate.tla117_0()
print(fechas_calculadas_tla117_0)