from datetime import datetime, date, timedelta
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

    def edges_0(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        date = master_date - relativedelta(months=3)
        # Regresa una lista con el formato
        conversion = date.strftime('%Y-%m-%d')
        return conversion

    def respuestas(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular la fecha tres meses atrás de masterDate
        datelast3Months = master_date - relativedelta(months=3)

        lastDayMonth = datelast3Months.replace(day=28) + timedelta(days=4)
        lastDayMonth = lastDayMonth - timedelta(days=lastDayMonth.day)

        # Regresa una lista con el formato
        datelast3Months = datelast3Months.strftime('%Y-%m-%d')
        lastDayMonth = lastDayMonth.strftime('%Y-%m-%d')

        return datelast3Months, lastDayMonth

    def prestamos_anuales_0(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        datelast3Months = master_date - relativedelta(months=3)
        datelastyear = datelast3Months - relativedelta(months=11)

        last_day_of_month = (datelast3Months.replace(day=1) + relativedelta(months=1)) - timedelta(days=1)

        # Regresa las variables en formato de fecha string
        last_day_of_month = last_day_of_month.strftime('%Y-%m-%d')
        datelastYear = datelastyear.strftime('%Y-%m-%d')

        listdates = [datelastYear, last_day_of_month]
        # Regresa una lista con el formato
        return listdates

    def prestamos_anuales_1(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        datelastyear = master_date - relativedelta(months=11)

        last_day_of_month = (master_date.replace(day=1) + relativedelta(months=1)) - timedelta(days=1)

        # Regresa las variables en formato de fecha string
        master_date_f = last_day_of_month.strftime('%Y-%m-%d')
        datelastYear = datelastyear.strftime('%Y-%m-%d')

        listdates = [datelastYear, master_date_f]
        # Regresa una lista con el formato
        return listdates

    def prestamos_recientes(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        datelastyear = master_date - relativedelta(months=2)

        last_day_of_month = (master_date.replace(day=1) + relativedelta(months=1)) - timedelta(days=1)

        # Regresa las variables en formato de fecha string
        last_day_of_month = last_day_of_month.strftime('%Y-%m-%d')
        datelastYear = datelastyear.strftime('%Y-%m-%d')

        listdates = [datelastYear, last_day_of_month]
        # Regresa una lista con el formato
        return listdates

    def solovinos(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        datelastyear = master_date - relativedelta(months=2)

        last_day_of_month = (master_date.replace(day=1) + relativedelta(months=1)) - timedelta(days=1)

        # Regresa las variables en formato de fecha string
        last_day_of_month = last_day_of_month.strftime('%Y-%m-%d')
        datelastYear = datelastyear.strftime('%Y-%m-%d')

        listdates = [datelastYear, last_day_of_month]
        # Regresa una lista con el formato
        return listdates
