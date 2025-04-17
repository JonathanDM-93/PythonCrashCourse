from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import math


class MasterDate:

    def __init__(self, Mater_date):
        self.Master_date = Mater_date

    def masterFormat(self):
        """Asignar el formato correcto a la fecha maestra para el resto de los calculos"""
        # Convertir la cadena de fecha a objeto datetime
        master_date = datetime.strptime(self.Master_date, '%Y-%m-%d')
        return master_date

    def clientes_Pyme(self):
        """Calcula tres meses antes de la fecha de MASTER_DATE y devuelve ambas fechas en una lista ordenada de menor a mayor"""
        master_date = self.masterFormat()
        date_three_months_ago = master_date - relativedelta(months=4)
        dates = [date_three_months_ago, master_date]
        dates.sort()
        return [date.strftime('%Y-%m-%d') for date in dates]


    def fechas_calculadas_1038(self):
        """Calcula el último día del mes 4 meses antes de MASTER_DATE y el primer día del mes 6 meses antes de MASTER_DATE"""
        master_date = self.masterFormat()

        # Calcular 4 meses atrás y el último día de ese mes
        date_four_months_ago = master_date - relativedelta(months=4)
        last_day_previous_3month = (date_four_months_ago.replace(day=1) + relativedelta(months=1)) - timedelta(days=1)
        last_day_previous_3month_str = last_day_previous_3month.strftime('%Y-%m-%d')

        # Calcular 6 meses atrás y el primer día de ese mes
        date_six_months_ago = master_date - relativedelta(months=6)
        date_six_months_first_day = date_six_months_ago.replace(day=1)
        date_six_months_first_day_str = date_six_months_first_day.strftime('%Y-%m-%d')

        # Regresa una lista con las fechas calculadas
        return [date_six_months_first_day_str, last_day_previous_3month_str]

    def dates_508(self):
        master_date = self.masterFormat()
        date_two_months_ago = master_date - relativedelta(months=2)
        date_one_month_ago = master_date - relativedelta(months=1)
        result = [
            date_two_months_ago.strftime('%Y-%m-%d'),
            date_one_month_ago.strftime('%Y-%m-%d'),
            master_date.strftime('%Y-%m-%d')
        ]
        return result

    def dates_813(self):
        master_date = self.masterFormat()
        date_two_months_ago = master_date - relativedelta(months=2)
        date_one_month_ago = master_date - relativedelta(months=1)
        result = [
            date_two_months_ago.strftime('%Y-%m-%d'),
            date_one_month_ago.strftime('%Y-%m-%d'),
            master_date.strftime('%Y-%m-%d')
        ]
        return result

    def tarjetas_813(self):
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


    def piBimDates_0_test(self):
        master_date = self.masterFormat()
        last_4_months = master_date - relativedelta(months=4)
        bimester = math.ceil(last_4_months.month / 2)
        start_month = (bimester - 1) * 2 + 1
        start_date = datetime(last_4_months.year, start_month, 1)
        start_date_str = start_date.strftime('%Y-%m-%d')
        return start_date_str

    def piBimDates_1_test(self):
        master_date = self.masterFormat()
        bimester = math.ceil(master_date.month / 2)
        previous_bimester = bimester - 1 if bimester > 1 else 6
        start_month = (previous_bimester - 1) * 2 + 1
        start_year = master_date.year if previous_bimester != 6 else master_date.year - 1
        start_date = datetime(start_year, start_month, 1)
        start_date_str = start_date.strftime('%Y-%m-%d')
        return start_date_str


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
            master_date - relativedelta(months=4),
            master_date - relativedelta(months=5),
            master_date - relativedelta(months=6)
        ]
        # Ordena las fechas
        dates.sort()
        # Regresa una lista con el formato
        return [date.strftime('%Y-%m-%d') for date in dates]
    ####################################################################################

    def edges_0(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        date = master_date - relativedelta(months=3)
        # Regresa una lista con el formato
        conversion = date.strftime('%Y-%m-%d')
        return conversion

    def prestamos_anuales_0(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        datelast3Months = master_date - relativedelta(months=4)
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

    def tarjeta(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        datelastyear = master_date - relativedelta(months=11)

        last_day_of_month = (master_date.replace(day=1) + relativedelta(months=1)) - timedelta(days=1)

        # Regresa las variables en formato de fecha string
        last_day_of_month = last_day_of_month.strftime('%Y-%m-%d')
        datelastYear = datelastyear.strftime('%Y-%m-%d')

        listdates = [datelastYear, last_day_of_month]
        # Regresa una lista con el formato
        return listdates

    def cambios_cadena_0(self):
        """Calcula tres meses atrás a partir de master_date"""
        master_date = self.masterFormat()

        # Calcular las fechas deseadas
        date = master_date - relativedelta(months=4)
        # Regresa una lista con el formato
        conversion = date.strftime('%Y-%m-%d')
        return conversion

    def last_four_months(self):
        master_date = self.masterFormat()
        date_minus_4_months = master_date - relativedelta(months=4)
        result_date_str = date_minus_4_months.strftime('%Y-%m-%d')
        return result_date_str

    def annual_edges_tr(self):
        master_date = self.masterFormat()
        date_minus_4_months = master_date - relativedelta(months=4)
        result_date_str = date_minus_4_months.strftime('%Y-%m-%d')
        return result_date_str




