# Clase Vehiculo
class Vehiculo:
    # Atributos
    patente: str
    anio: int
    _en_taller: bool

    # Constructor
    def __init__(self, patente: str, anio: int, _en_taller: bool = False):
        # Validar patente
        if not isinstance(patente, str) or not patente.strip():
            raise ValueError("La patente debe ser texto no vacío.")

        # Validar año
        if not isinstance(anio, int) or anio < 1900:
            raise ValueError("El año debe ser un entero mayor a 1900.")

        # Validar estado en taller
        if not isinstance(_en_taller, bool):
            raise TypeError("El estado _en_taller debe ser booleano.")

        # Asignación de atributos
        self.patente = patente
        self.anio = anio
        self._en_taller = _en_taller
