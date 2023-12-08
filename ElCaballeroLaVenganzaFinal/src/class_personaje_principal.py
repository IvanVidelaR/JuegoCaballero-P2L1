import pygame
from class_personaje import *
from class_caballero_malvado import *

class Personaje_principal(Personaje):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, animaciones: dict, tipo_animacion: str) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, tipo_animacion)

        self.conteo_salto = 0
        self.puntuacion = 0
        self.vidas = 3
        self.sonido_pisando = pygame.mixer.Sound(r"src\Assets\sounds\caballero_caida.WAV")
        self.sonido_daño_personaje_principal = pygame.mixer.Sound(r"src\Assets\sounds\colision_caballero.wav")
        self.ya_recibio_daño_personaje_principal = False
        self.acaba_de_pisar = True

    def saltar(self):
        self.desplazamiento_y = self.gravedad * -10

        if self.conteo_salto == 1:
            self.conteo_caida = 0

    def actualizar_animacion_personaje(self, pantalla):
        if self.daño:
            if self.ya_recibio_daño_personaje_principal == False:
                    self.sonido_daño_personaje_principal.play()
                    self.ya_recibio_daño_personaje_principal = True
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "recibir_daño_derecha")
            else:
                self.dibujar_animacion(pantalla, "recibir_daño_izquierda")
        elif self.desplazamiento_y < 0:
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "saltar_derecha")
            else:
                self.dibujar_animacion(pantalla, "saltar_izquierda")
        elif self.desplazamiento_y > self.gravedad:
            self.esta_saltando = True
            self.acaba_de_pisar = True
            self.ya_recibio_daño_personaje_principal = False
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "caer_derecha")
            else:
                self.dibujar_animacion(pantalla, "caer_izquierda")
        elif self.velocidad != 0:
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "correr_derecha")
            else:
                self.dibujar_animacion(pantalla, "correr_izquierda")
        else:
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "quieto_derecha")
            else:
                self.dibujar_animacion(pantalla, "quieto_izquierda")

    def verificar_eventos_personaje(self, lista_teclas, diccionario_items_juego):
        self.velocidad = 0
    
        if lista_teclas[pygame.K_d] and not(lista_teclas[pygame.K_a]):
            #El personaje está moviendo a la derecha
            self.personaje_derecha = True
            self.velocidad = 6
            self.mover(self.velocidad)
        if lista_teclas[pygame.K_a] and not(lista_teclas[pygame.K_d]):
            #El personaje está moviendo a la izquierda
            self.personaje_derecha = False
            self.velocidad = 6
            self.mover(-self.velocidad)
        if (lista_teclas[pygame.K_SPACE] or lista_teclas[pygame.K_w]) and self.esta_saltando == False:
            self.esta_saltando = True
            self.saltar()
        if (lista_teclas[pygame.K_e]):
            if self.disparo == False: 
                self.lanzar_proyectil(diccionario_items_juego)
                self.disparo = True 

    def actualizar(self, pantalla, fps, lista_teclas, lista_plataformas, lista_items, lista_enemigos, diccionario_items_juego):
        self.aplicar_gravedad(fps)
        self.manejar_daño(fps)
        self.manejar_tiempo_disparo(fps)
        self.verificar_colision_piso(lista_plataformas)
        self.verificar_colision_items(lista_items)
        self.verificar_colision_proyectil(lista_enemigos)
        self.verificar_colision_enemigos(lista_enemigos)
        self.verificar_eventos_personaje(lista_teclas, diccionario_items_juego)
        self.actualizar_animacion_personaje(pantalla)

    def verificar_colision_piso(self, lista_plataformas):
        for plataforma in lista_plataformas:
            if plataforma.esta_visible:
                if self.lados["bottom"].colliderect(plataforma.lados["top"]) and self.desplazamiento_y > 0 and plataforma.tipo_animacion != "plataforma_pared":
                    if self.acaba_de_pisar:
                        self.sonido_pisando.play()
                    for lado in self.lados:
                        if lado == "top":
                            self.lados[lado].bottom = self.lados["main"].top + 15
                        else:
                            self.lados[lado].bottom = plataforma.lados["main"].top
                        self.conteo_caida = 0
                        self.desplazamiento_y = 0
                        self.conteo_salto = 0
                        self.esta_saltando = False
                        self.acaba_de_pisar = False
                elif self.lados["top"].colliderect(plataforma.lados["bottom"]) and self.desplazamiento_y < 0 and plataforma.tipo_animacion != "plataforma_pared":
                    self.conteo_salto = 0
                    self.conteo_caida = 0
                    self.desplazamiento_y *= -1
                    #self.rectangulo.top = piso.rectangulo.bottom
                elif self.lados["right"].colliderect(plataforma.lados["left"]):
                    #el personaje esta moviendo a la derecha
                    self.esta_saltando = True
                    self.mover(-self.velocidad)
                    
                elif self.lados["left"].colliderect(plataforma.lados["right"]):
                    #el personaje esta moviendo a la izquierda
                    self.esta_saltando = True
                    self.mover(self.velocidad)
            
    def verificar_colision_items(self, lista_items):
        for item in lista_items:
            if item.esta_visible:
                if self.lados["main"].colliderect(item.lados["main"]):
                    item.aplicar_efecto(self)
                    if item.tipo_animacion != "pinchos_item" and item.tipo_animacion != "sierras_item":
                        lista_items.remove(item)
                    else:
                        self.daño = True
            
        return lista_items
    
    def verificar_colision_enemigos(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.lados["bottom"].colliderect(enemigo.lados["top"]) and self.desplazamiento_y > 0:
                if self.acaba_de_pisar:
                        self.sonido_pisando.play()
                for lado in self.lados:
                    if lado == "top":
                        self.lados[lado].bottom = self.lados["main"].top + 15
                    else:
                        self.lados[lado].bottom = enemigo.lados["main"].top
                    self.conteo_caida = 0
                    self.desplazamiento_y *= -1
                    self.conteo_salto = 0
                    self.esta_saltando = False
                if enemigo.que_es == "Caballero_malvado":
                    self.daño = True
                    self.vidas -= 1
                else:
                    enemigo.daño = True
                    enemigo.vidas -= 1
                    
                if enemigo.vidas == 0:
                    self.puntuacion += 10
                    enemigo.desaparecer()
            elif self.lados["right"].colliderect(enemigo.lados["left"]):
                if isinstance(enemigo, Caballero_malvado):
                    self.vidas = 0
                else:
                    self.vidas -= 1
                self.esta_saltando = True
                self.daño = True
                self.mover(self.velocidad *-6)
                #ENEMIGO:
                self.vida_restada = False
                self.esta_saltando = True
                self.velocidad = -self.velocidad
            elif self.lados["left"].colliderect(enemigo.lados["right"]):
                if isinstance(enemigo, Caballero_malvado):
                    self.vidas = 0
                else:
                    self.vidas -= 1
                self.esta_saltando = True
                self.daño = True
                self.mover(self.velocidad *6)
        
        return lista_enemigos
