import pygame
from class_objeto_juego import *

class Plataforma(Objeto_Juego):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, diccionario_plataformas: dict, tipo_animacion:str, visible:bool) -> None:
        self.esta_visible = visible
        self.daño = False
        self.contador_daño = 0
        self.sonido_impacto_plataforma = pygame.mixer.Sound(r"src\Assets\sounds\impacto_plataformas.wav")
        self.sonido_impacto_caja = pygame.mixer.Sound(r"src\Assets\sounds\caja_romper.wav")
        super().__init__(tamaño, posicion_inicial, diccionario_plataformas, tipo_animacion)

    def verificar_colision_proyectiles(self, lista_proyectiles:list) -> bool:
        for proyectil in lista_proyectiles:
            if self.lados["main"].colliderect(proyectil.lados["main"]):
                if self.tipo_animacion == "caja_recibir_daño" or self.tipo_animacion == "caja_quieto":
                    self.daño = True
                    self.sonido_impacto_caja.play()
                else:
                    self.sonido_impacto_plataforma.play()
                lista_proyectiles.remove(proyectil)
        
        return lista_proyectiles

    def actualizar(self, pantalla, personaje, lista_plataformas: list, fps: int, enemigos: list):
        if self.esta_visible:
            self.verificar_colision_proyectiles(personaje.lista_proyectiles)
            for enemigo in enemigos:
                self.verificar_colision_proyectiles(enemigo.lista_proyectiles)
            if self.tipo_animacion != "caja_recibir_daño" and self.tipo_animacion != "caja_quieto":
                super().actualizar(pantalla)
            else:
                if self.daño:
                    self.dibujar_animacion(pantalla, "caja_recibir_daño")
                    self.contador_daño += 1
                    if self.contador_daño > fps:
                        lista_plataformas.remove(self)
                else:
                    self.dibujar_animacion(pantalla, "caja_quieto")
        elif personaje.vidas < 2:
            self.esta_visible = True
        else:
            pass