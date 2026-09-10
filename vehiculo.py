# Clase Vehiculo para representar vehículos en el taller
class Vehiculo:
    # Atributo privado que almacena la patente
    __patente: str
    # Atributo privado que almacena el año del vehículo
    __anio: int
    # Atributo privado que indica si el vehículo está en el taller
    __en_taller: bool

    # Constructor de la clase Vehiculo con validaciones
    def __init__(self, patente: str, anio: int, _en_taller: bool = False):
        # Validar que la patente sea una cadena de texto no vacía
        if not isinstance(patente, str) or not patente.strip():
            # Lanzar excepción si la patente no es válida
            raise ValueError("La patente debe ser texto no vacío.")

        # Validar que el año sea un número entero mayor a 1900
        if not isinstance(anio, int) or anio < 1900:
            # Lanzar excepción si el año no es válido
            raise ValueError("El año debe ser un entero mayor a 1900.")

        # Validar que el estado en taller sea de tipo booleano
        if not isinstance(_en_taller, bool):
            # Lanzar excepción si el estado en taller no es booleano
            raise TypeError("El estado _en_taller debe ser booleano.")

        # Asignar la patente al atributo privado __patente
        self.__patente = patente
        # Asignar el año al atributo privado __anio
        self.__anio = anio
        # Asignar el estado en taller al atributo privado __en_taller
        self.__en_taller = _en_taller

    # El decorador @property define un getter que permite acceder a la patente como un atributo (auto.patente) protegiendo __patente
    @property
    def patente(self) -> str:
        # Retornar el valor del atributo privado __patente
        return self.__patente

    # El decorador @property define un getter que permite acceder al año como un atributo (auto.anio) protegiendo __anio
    @property
    def anio(self) -> int:
        # Retornar el valor del atributo privado __anio
        return self.__anio

    # El decorador @property define un getter que permite consultar el estado como un atributo (auto.en_taller) protegiendo __en_taller
    @property
    def en_taller(self) -> bool:
        # Retornar el valor del atributo privado __en_taller
        return self.__en_taller

    # Método para registrar el ingreso al taller
    def ingresar(self) -> None:
        # Cambiar el estado del vehículo a True (en taller)
        self.__en_taller = True

    # Método para registrar la entrega del vehículo
    def entregar(self) -> None:
        # Cambiar el estado del vehículo a False (fuera de taller)
        self.__en_taller = False

    # Método para obtener la tarifa por hora genérica del vehículo
    def tarifa_hora(self) -> int:
        # Retornar el valor genérico de 5000
        return 5000
