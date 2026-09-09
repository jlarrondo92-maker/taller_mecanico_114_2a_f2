from vehiculo import Vehiculo

# Creación de dos vehículos
v1 = Vehiculo(patente="KXPR84", anio=2019)
v2 = Vehiculo(patente="JKLM12", anio=2016)

# Llamar a ingresar() solo en v1
v1.ingresar()

# Imprimir patente y si está en el taller usando las properties
print(f"Vehículo 1 - Patente: {v1.patente}, ¿En taller?: {v1.en_taller}")
print(f"Vehículo 2 - Patente: {v2.patente}, ¿En taller?: {v2.en_taller}")
