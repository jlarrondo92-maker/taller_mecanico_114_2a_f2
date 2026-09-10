from vehiculo import Vehiculo
from auto import Auto
from moto import Moto
from camion import Camion


v=Vehiculo("1234" ,1930)
v.ingresar()
print("Vehiculo_en_taller")


print(v.en_taller)

print(v.tarifa_hora())

v.entregar()

print(v.en_taller)



# Creación de dos vehículos
v1 = Vehiculo(patente="KXPR84", anio=2019)
v2 = Vehiculo(patente="JKLM12", anio=2016)

# Llamar a ingresar() solo en v1
v1.ingresar()

# Imprimir patente y si está en el taller usando las properties
print(f"Vehículo 1 - Patente: {v1.patente}, ¿En taller?: {v1.en_taller}")
print(f"Vehículo 2 - Patente: {v2.patente}, ¿En taller?: {v2.en_taller}")
