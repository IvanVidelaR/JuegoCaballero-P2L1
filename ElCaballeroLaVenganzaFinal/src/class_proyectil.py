from class_objeto_juego import *
from class_items import *

class Proyectil(Objeto_Juego):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, diccionario_objetos_juego: dict, tipo_animacion: str, velocidad: int) -> None:
        super().__init__(tamaño, posicion_inicial, diccionario_objetos_juego, tipo_animacion)
        self.velocidad = velocidad

    def actualizar(self, pantalla):
        self.mover(self.velocidad)
        super().actualizar(pantalla)
        

