from handleDates import MasterDate

# Creo la instancia a partir de la clase
MASTER_DATE = "2023-10-01"
Ingresar_MasterDate = MasterDate(MASTER_DATE)
FechaCorrect = Ingresar_MasterDate.masterFormat()
print(FechaCorrect)

fechas_calculadas_tla117_1 = Ingresar_MasterDate.tla117_1()
print(fechas_calculadas_tla117_1)

fechas_calculadas_tla117_0 = Ingresar_MasterDate.tla117_0()
print(fechas_calculadas_tla117_0)

fecha_calculada_edges_0 = Ingresar_MasterDate.edges_0()
print(f"FECHAS EDGES_O: {fecha_calculada_edges_0}")

fecha_calculada_campTracking = Ingresar_MasterDate.respuestas()
print(f"FECHA RESPUESTAS: {fecha_calculada_campTracking}")

fecha_calculada_prestamos_anuales_0 = Ingresar_MasterDate.prestamos_anuales_0()
print(f"FECHA PRESTAMOS ANUALES_0: {fecha_calculada_prestamos_anuales_0}")

fecha_calculada_prestamos_anuales_1 = Ingresar_MasterDate.prestamos_anuales_1()
print(f"FECHA PRESTAMOS ANUALES_1: {fecha_calculada_prestamos_anuales_1}")

fecha_calculada_prestamos_recientes = Ingresar_MasterDate.prestamos_recientes()
print(f"FECHA PRESTAMOS RECIENTES: {fecha_calculada_prestamos_recientes}")

fecha_calculada_solovinos = Ingresar_MasterDate.solovinos()
print(f"FECHA SOLOVINOS: {fecha_calculada_solovinos}")

fecha_calculada_tarjeta = Ingresar_MasterDate.tarjeta()
print(f"FECHA TARJETA: {fecha_calculada_tarjeta}")

bimestre_calculado1 = Ingresar_MasterDate.piBimDates_1()
print(f"FECHA BIMESTRE_1: {bimestre_calculado1}")

bimestre_calculado0 = Ingresar_MasterDate.piBimDates_0()
print(f"FECHA BIMESTRE_0: {bimestre_calculado0}")

fecha_calculada_cambios_cadena = Ingresar_MasterDate.cambios_cadena_0()
print(f"FECHA CAMBIOS CADENA: {fecha_calculada_cambios_cadena}")

three_months_beforeDate = Ingresar_MasterDate.last_three_months()
print(f"FECHA THREE MONTHS: {three_months_beforeDate}")