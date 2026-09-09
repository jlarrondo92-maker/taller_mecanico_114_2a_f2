# Clase LineaDetalle
class LineaDetalle:
    # Atributo que almacena la cantidad de unidades
    cantidad: int
    # Atributo que almacena el precio unitario
    precio_unitario: float

    # Constructor que recibe cantidad y precio_unitario como parámetros
    def __init__(self, cantidad: int, precio_unitario: float):
        # Asignación del parámetro cantidad al atributo de la instancia
        self.cantidad = cantidad
        # Asignación del parámetro precio_unitario al atributo de la instancia
        self.precio_unitario = precio_unitario

    # Método subtotal sin parámetros que calcula el valor total de la línea
    def subtotal(self) -> float:
        # Retorna el resultado de multiplicar la cantidad por el precio unitario
        return self.cantidad * self.precio_unitario
