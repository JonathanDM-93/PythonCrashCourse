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
print(f" FECHAS EDGES_O: {fecha_calculada_edges_0}")

fecha_calculada_campTracking = Ingresar_MasterDate.campaingTracking()
print(f"FECHA CAMPTRACKING: {fecha_calculada_campTracking}")

