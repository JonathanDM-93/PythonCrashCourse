from handleDates_Class import MasterDate

# Creo la instancia a partir de la clase
MASTER_DATE = "2023-11-01"

# Crear isntancia de la clase MasterDate
Ingresar_MasterDate = MasterDate(MASTER_DATE)
FechaCorrect = Ingresar_MasterDate.masterFormat()
print(FechaCorrect)

bimestre_calculado0 = Ingresar_MasterDate.piBimDates()
print(f"FECHA BIMESTRE_0: {bimestre_calculado0}")