from class_objeto_juego import *
from class_personaje import *

class Item(Objeto_Juego):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, diccionario_plataformas: dict, tipo_animacion:str) -> None:
        super().__init__(tamaño, posicion_inicial, diccionario_plataformas, tipo_animacion)

    def aplicar_efecto(self, personaje):
        pass


