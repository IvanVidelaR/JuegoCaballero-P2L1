from class_items import *
import pygame

class Recompensa(Item):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, diccionario_plataformas: dict, tipo_animacion: str) -> None:
        self.esta_visible = True
        if tipo_animacion == "caliz_vino_item":
            self.esta_visible = False
        super().__init__(tamaño, posicion_inicial, diccionario_plataformas, tipo_animacion)
        self.sonido_bolsas_oro_item = pygame.mixer.Sound(r"src\Assets\sounds\recoleccion_monedas.mp3")
        self.sonido_caliz_vino_item = pygame.mixer.Sound(r"src\Assets\sounds\recoleccion_caliz.WAV")
        self.sonido_espada_proyectil_item = pygame.mixer.Sound(r"src\Assets\sounds\recoleccion_espada.mp3")

    def aplicar_efecto(self, personaje):
        if self.tipo_animacion == "bolsas_oro_item":
            self.sonido_bolsas_oro_item.play()
            personaje.puntuacion += 200
        elif self.tipo_animacion == "espada_proyectil_item":
            self.sonido_espada_proyectil_item.play()
            personaje.cantidad_proyectiles += 2
        elif self.tipo_animacion == "caliz_vino_item":
            self.sonido_caliz_vino_item.play()
            personaje.vidas += 1
    
    def actualizar(self, pantalla, personaje):
        if self.esta_visible:
            super().actualizar(pantalla)
        elif personaje.vidas < 2:
            self.esta_visible = True