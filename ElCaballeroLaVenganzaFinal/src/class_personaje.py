import pygame
from class_objeto_juego import *
from class_proyectil import *

class Personaje(Objeto_Juego):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, animaciones: dict, tipo_animacion:str) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, tipo_animacion)
        #GRAVEDAD
        self.gravedad = 1
        self.desplazamiento_y = 0
        self.conteo_caida = 0
        self.velocidad = 0
        self.personaje_derecha = True
        self.esta_saltando = True
        self.colisionando_pared = False
        self.daño = False
        self.disparo = False
        self.conteo_daño = 0
        self.cantidad_proyectiles = 1
        self.lista_proyectiles = []
        self.conteo_tiempo_disparo = 0
        self.segundos_entre_disparo = 2
        self.sonido_lanzar_espada = pygame.mixer.Sound("src\Assets\sounds\lanzar_espada.wav")
        #cambiar todo por contador en vez de conteo  
        
    def aplicar_gravedad(self, fps):
        self.desplazamiento_y += self.conteo_caida / fps * self.gravedad
        
        for lado in self.lados:
            self.lados[lado].y += self.desplazamiento_y

        self.conteo_caida += 1
    
    def manejar_daño(self, fps):
        if self.daño:
            self.conteo_daño += 1
        if self.conteo_daño > fps:
            self.daño = False
            self.conteo_daño = 0

    def manejar_tiempo_disparo(self, fps):
        if self.disparo:
            self.conteo_tiempo_disparo += 1
            if self.conteo_tiempo_disparo > fps * self.segundos_entre_disparo:
                self.disparo = False
                self.conteo_tiempo_disparo = 0
    
    def lanzar_proyectil(self, diccionario_items_juego):
        if self.cantidad_proyectiles > 0 :
            self.sonido_lanzar_espada.play()
            if self.personaje_derecha:
                x = self.lados["right"].x
                proyectil = Proyectil((30,15),(x, self.lados["bottom"].y - 10), diccionario_items_juego, "proyectil_derecha_item", 10)
            else:
                x = self.lados["left"].x - self.ancho
                proyectil = Proyectil((30,15),(x, self.lados["bottom"].y - 10), diccionario_items_juego, "proyectil_izquierda_item", -10)
            self.lista_proyectiles.append(proyectil)
            self.cantidad_proyectiles -= 1
            self.disparo = True

    def verificar_colision_proyectil(self, objetivo):
        if type(objetivo) == list:
            for personaje in objetivo:
                for proyectil in self.lista_proyectiles:
                    if personaje.lados["main"].colliderect(proyectil.lados["main"]):
                        self.lista_proyectiles.remove(proyectil)
                        personaje.daño = True
                        personaje.conteo_daño = 0
                        if personaje.que_es == "Esqueleto" or personaje.que_es == "Duende":
                            personaje.vidas -= 2
                        else:
                            personaje.vidas -= 1
                        self.puntuacion += 100
                        if personaje.vidas <= 0:
                            personaje.desaparecer()
        else:
            for proyectil in self.lista_proyectiles:
                    if objetivo.lados["main"].colliderect(proyectil.lados["main"]):
                        self.lista_proyectiles.remove(proyectil)
                        objetivo.daño = True
                        objetivo.conteo_daño = 0
                        objetivo.vidas -= 1


