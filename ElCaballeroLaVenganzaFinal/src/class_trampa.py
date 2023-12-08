from class_items import *

class Trampa(Item):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, diccionario_plataformas: dict, tipo_animacion: str) -> None:
        self.esta_visible = True
        super().__init__(tamaño, posicion_inicial, diccionario_plataformas, tipo_animacion)

    def aplicar_efecto(self, personaje):
        if self.tipo_animacion == "pinchos_item" or self.tipo_animacion == "sierras_item":
            personaje.desplazamiento_y = -20
            personaje.vidas -= 1
        