import random
from pygame import *
from class_personaje import * 

class Personaje_enemigo(Personaje):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, animaciones: dict, tipo_animacion: str) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, tipo_animacion)

        self.eleccion = False
        self.vida_restada = False
        self.vidas = 2
        self.conteo_eleccion = 0
        self.que_es = "Duende"
        self.sonido_enemigo_puerta = pygame.mixer.Sound(r"src\Assets\sounds\puerta_enemigos_cerrar.wav")
        self.sonido_daño_duende = pygame.mixer.Sound(r"src\Assets\sounds\colision_duende.ogg")
        self.sonido_daño_caballero_malvado = pygame.mixer.Sound(r"src\Assets\sounds\colision_boss_final.wav")
        self.sonido_daño_esqueleto = pygame.mixer.Sound(r"src\Assets\sounds\colision_esqueleto.wav")
        self.ya_recibio_daño_duende = False
        self.ya_recibio_daño_esqueleto = False
        self.ya_recibio_daño_caballero_malvado = False

    def actualizar_animacion_personaje(self, pantalla):
        if self.velocidad > 0:
            self.personaje_derecha = True
        else:
            self.personaje_derecha = False

        if self.daño:
            if self.que_es == "Duende":
                if self.ya_recibio_daño_duende == False:
                    self.sonido_daño_duende.play()
                    self.ya_recibio_daño_duende = True
            elif self.que_es == "Caballero_malvado":
                if self.ya_recibio_daño_caballero_malvado == False:
                    self.sonido_daño_caballero_malvado.play()
                    self.ya_recibio_daño_caballero_malvado = True
            elif self.que_es == "Esqueleto":
                if self.ya_recibio_daño_esqueleto == False:
                    self.sonido_daño_esqueleto.play()
                    self.ya_recibio_daño_esqueleto = True
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "recibir_daño_derecha")
            else:
                self.dibujar_animacion(pantalla, "recibir_daño_izquierda")
        elif self.desplazamiento_y > self.gravedad:
            self.esta_saltando = True
            self.ya_recibio_daño_duende = False
            self.ya_recibio_daño_esqueleto = False
            self.ya_recibio_daño_caballero_malvado = False
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "caer_derecha")
            else:
                self.dibujar_animacion(pantalla, "caer_izquierda")
        else:
            if self.personaje_derecha:
                self.dibujar_animacion(pantalla, "correr_derecha")
            else:
                self.dibujar_animacion(pantalla, "correr_izquierda")

    def elegir_direccion_aleatoriamente(self):

        if self.eleccion == False:
            self.velocidad = random.choice([-6, 6, -4, 4, -2, 2])
            self.eleccion = True

    def manejar_direccion_aleatoria(self, fps):
        if self.eleccion:
            self.conteo_eleccion += 1
        if self.conteo_eleccion > fps * 5:
            self.eleccion = False
            self.conteo_eleccion = 0

    def verificar_colision_piso(self, lista_plataformas):
        for plataforma in lista_plataformas:
            if plataforma.esta_visible:
                if self.lados["bottom"].colliderect(plataforma.lados["top"]) and plataforma.tipo_animacion != "plataforma_pared" and plataforma.tipo_animacion != "plataforma_techo":
                    for lado in self.lados:
                        if lado == "top":
                            self.lados[lado].bottom = self.lados["main"].top + 15
                        else:
                            self.lados[lado].bottom = plataforma.lados["main"].top
                        self.conteo_caida = 0
                        self.desplazamiento_y = 0
                        self.esta_saltando = False
                        self.vida_restada = False
                        self.elegir_direccion_aleatoriamente()
                elif self.lados["top"].colliderect(plataforma.lados["bottom"]) and self.desplazamiento_y < 0 and plataforma.tipo_animacion != "plataforma_pared":
                    self.conteo_salto = 0
                    self.conteo_caida = 0
                    self.desplazamiento_y *= -1
                    self.vida_restada = False
                elif self.lados["right"].colliderect(plataforma.lados["left"]) and plataforma.tipo_animacion != "plataforma_puerta_enemigos":
                    #el personaje esta moviendo a la derecha
                    self.esta_saltando = True
                    self.velocidad = -self.velocidad
                elif self.lados["left"].colliderect(plataforma.lados["right"]) and plataforma.tipo_animacion != "plataforma_puerta_enemigos":
                    #el personaje esta moviendo a la izquierda
                    self.esta_saltando = True
                    self.velocidad = -self.velocidad
                elif self.lados["right"].colliderect(plataforma.lados["main"]) and plataforma.tipo_animacion == "plataforma_puerta_enemigos":
                    self.sonido_enemigo_puerta.play()
                    self.desaparecer()
                elif self.lados["left"].colliderect(plataforma.lados["main"]) and plataforma.tipo_animacion == "plataforma_puerta_enemigos":
                    self.sonido_enemigo_puerta.play()
                    self.desaparecer()

    def verificar_colision_jugador(self, jugador):
        if self.lados["bottom"].colliderect(jugador.lados["top"]):
            for lado in self.lados:
                if lado == "top":
                    self.lados[lado].bottom = self.lados["main"].top + 15
                else:
                    self.lados[lado].bottom = jugador.lados["main"].top
                self.conteo_caida = 0
                self.esta_saltando = False
                if self.vida_restada == False: #ARREGLA BUG DE QUE RESTABA 5 VIDAS POR COLISIONAR MUCHO
                    jugador.vidas -= 1
                    self.vida_restada = True
                if self.que_es == "Caballero_Malvado":
                    jugador.vidas = 0
                jugador.daño = True
                self.desplazamiento_y *= -1
                jugador.conteo_salto = 0
                jugador.conteo_caida = 0
                jugador.desplazamiento_y *= -1
                self.elegir_direccion_aleatoriamente()
        elif self.lados["right"].colliderect(jugador.lados["left"]):
            #el personaje esta moviendo a la derecha
            self.vida_restada = False
            self.esta_saltando = True
            self.velocidad = -self.velocidad
        elif self.lados["left"].colliderect(jugador.lados["right"]):
            #el personaje esta moviendo a la izquierda
            self.vida_restada = False
            self.esta_saltando = True
            self.velocidad = -self.velocidad

    def actualizar(self, pantalla, fps, lista_plataformas, jugador):
        self.mover(self.velocidad)
        self.aplicar_gravedad(fps)
        self.manejar_daño(fps)
        self.manejar_direccion_aleatoria(fps)
        self.verificar_colision_piso(lista_plataformas)
        self.verificar_colision_jugador(jugador)
        self.actualizar_animacion_personaje(pantalla)

    def desaparecer(self):
        if self.que_es == "Duende" or self.que_es == "Esqueleto":
            self.vidas = 2
        
        x = random.randrange(400, 1280 - 400, 60)
        y = random.randrange(-500, 0, 50)
        self.rectangulo.x = x
        self.rectangulo.y = y
        for lado in self.lados:
            if lado == "top":
                self.lados[lado].x = x
                self.lados[lado].y = y    
            elif lado == "bottom":
                self.lados[lado].x = x
                self.lados[lado].y = y + self.alto
            elif lado == "right":
                self.lados[lado].x = x + self.ancho - self.lados[lado].width
                self.lados[lado].y = y
            elif lado == "left":
                self.lados[lado].x = x
                self.lados[lado].y = y 