from handleDates import MasterDate

# Creo la instancia a partir de la clase
MASTER_DATE = "2025-01-01"
Ingresar_MasterDate = MasterDate(MASTER_DATE)
FechaCorrect = Ingresar_MasterDate.masterFormat()
print(FechaCorrect)

dates_ClientsPyme = Ingresar_MasterDate.clientes_Pyme()
print(f"FECHA CLIENTES PYME_0: {dates_ClientsPyme[0]}")
print(f"FECHA CLIENTES PYME_1: {dates_ClientsPyme[1]}")

dates_1038 = Ingresar_MasterDate.fechas_calculadas_1038()
print(f"FECHA 1038_0: {dates_1038}")

dates_508 = Ingresar_MasterDate.dates_508()
print(f"FECHA 508: {dates_508}")

prestamos_anuales_0 = Ingresar_MasterDate.prestamos_anuales_0()
print(f"FECHA PRESTAMOS ANUALES_0: {prestamos_anuales_0}")
prestamos_anuales_1 = Ingresar_MasterDate.prestamos_anuales_1()
print(f"FECHA PRESTAMOS ANUALES_1: {prestamos_anuales_1}")

prestamos_recientes_Dates = Ingresar_MasterDate.prestamos_recientes()
print(f"FECHA PRESTAMOS RECIENTES: {prestamos_recientes_Dates}")

solovinos_Dates = Ingresar_MasterDate.solovinos()
print(f"FECHA SOLOVINOS: {solovinos_Dates}")

dates_813 = Ingresar_MasterDate.dates_508()
print(f"FECHA 813: {dates_813}")

tarjeta_Dates = Ingresar_MasterDate.tarjetas_813()
print(f"FECHA TARJETA: {tarjeta_Dates}")

bim_0_dates = Ingresar_MasterDate.piBimDates_0_test()
print(f"FECHA BIMESTRE_0: {bim_0_dates}")

bim_1_dates = Ingresar_MasterDate.piBimDates_1_test()
print(f"FECHA BIMESTRE_1: {bim_1_dates}")

dates_cam_cadena_0 = Ingresar_MasterDate.cambios_cadena_0()
print(f"FECHA CAMBIOS CADENA: {dates_cam_cadena_0}")

dates_last_four_months = Ingresar_MasterDate.last_four_months()
print(f"FECHA LAST FOUR MONTHS: {dates_last_four_months}")

dates_annual_edges = Ingresar_MasterDate.annual_edges_tr()
print(f"FECHA ANNUAL EDGES: {dates_annual_edges}")

dates_tla117_0 = Ingresar_MasterDate.tla117_0()
print(f"FECHA TLA117_0: {dates_tla117_0}")

dates_tla117_1 = Ingresar_MasterDate.tla117_1()
print(f"FECHA TLA117_1: {dates_tla117_1}")
dates_tla117_0 = Ingresar_MasterDate.tla117_0()
print(f"FECHA TLA117_0: {dates_tla117_0}")

dates_tla117_1 = Ingresar_MasterDate.tla117_1()
print(f"FECHA TLA117_1: {dates_tla117_1}")

"""
fechas_calculadas_tla117_1 = Ingresar_MasterDate.tla117_1()
print(fechas_calculadas_tla117_1)

fechas_calculadas_tla117_0 = Ingresar_MasterDate.tla117_0()
print(fechas_calculadas_tla117_0)

fecha_calculada_edges_0 = Ingresar_MasterDate.edges_0()
print(f"FECHAS EDGES_O: {fecha_calculada_edges_0}")

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



"""