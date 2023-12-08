import pygame
import sys
import random
from modo_programador import *
from class_esqueleto import *
from class_caballero_malvado import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, lista_items, lista_enemigos, imagen_fondo, fps, lista_tamaños, fuente_texto, diccionario_items_juego):
        self.lista_tamaños = lista_tamaños
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.items = lista_items
        self.enemigos = lista_enemigos
        self.img_fondo = imagen_fondo
        self.fps = fps
        self.fuente_texto = fuente_texto
        self.diccionario_items = diccionario_items_juego
        self.tiempo_restante = fps * 2
        self.puntuacion = 0
        self.vidas_enemigo = 5
    
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_TAB:
                    cambiar_modo()

        lista_teclas = self.leer_inputs()
        self.actualizar_pantalla(lista_teclas)

    def dibujar_rectangulos(self):
        if get_mode():
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Red", self.jugador.lados[lado], 3)
            for enemigo in self.enemigos:
                if isinstance(enemigo, Esqueleto) or isinstance(enemigo, Caballero_malvado):
                    for proyectil in enemigo.lista_proyectiles:
                        for lado in proyectil.lados:
                            pygame.draw.rect(self._slave, "Yellow", proyectil.lados[lado], 3)
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, "Red", enemigo.lados[lado], 3)
            for plataforma in self.plataformas:
                if plataforma.esta_visible:
                    for lado in plataforma.lados:
                        pygame.draw.rect(self._slave, "Green", plataforma.lados[lado], 3)
            for item in self.items:
                if item.esta_visible:
                    for lado in item.lados:
                        pygame.draw.rect(self._slave, "Blue", item.lados[lado], 3)
            for proyectil in self.jugador.lista_proyectiles:
                for lado in proyectil.lados:
                    pygame.draw.rect(self._slave, "Yellow", proyectil.lados[lado], 3)
            self.dibujar_grilla()
        
        pygame.draw.rect(self._slave, "Black", (0, 0, self.lista_tamaños[0], 64))


    def leer_inputs(self):
        lista_teclas = pygame.key.get_pressed()

        return lista_teclas

    def actualizar_pantalla(self, lista_teclas):
        self._slave.blit(self.img_fondo, (0,0))
        self.jugador.actualizar(self._slave, self.fps, lista_teclas, self.plataformas, self.items, self.enemigos, self.diccionario_items)
        for item in self.items:
            if item.tipo_animacion == "pinchos_item" or item.tipo_animacion == "sierras_item":
                item.actualizar(self._slave)
            else:
                item.actualizar(self._slave, self.jugador)
        for plataforma in self.plataformas:
            plataforma.actualizar(self._slave, self.jugador, self.plataformas, self.fps, self.enemigos)
        for enemigo in self.enemigos:
            if isinstance(enemigo, Esqueleto) or isinstance(enemigo, Caballero_malvado):
                enemigo.actualizar(self._slave, self.fps, self.plataformas, self.jugador, self.diccionario_items)
                for proyectil in enemigo.lista_proyectiles:
                    proyectil.actualizar(self._slave)
            else:
                enemigo.actualizar(self._slave, self.fps, self.plataformas, self.jugador)
        for proyectil in self.jugador.lista_proyectiles:
            proyectil.actualizar(self._slave)
        self.dibujar_rectangulos()
        self.dibujar_texto_puntuacion_vidas()


    def dibujar_grilla(self):
        for linea in range(0, 20):
            pygame.draw.line(self._slave, "White", (0, linea * self.lista_tamaños[2]), (self.lista_tamaños[0], linea * self.lista_tamaños[2]))
            pygame.draw.line(self._slave, "White", (linea * self.lista_tamaños[2], 0), (linea * self.lista_tamaños[2], self.lista_tamaños[0]))
    
    def dibujar_texto_puntuacion_vidas(self):
        for enemigo in self.enemigos:
            if isinstance(enemigo, Caballero_malvado):
                self.vidas_enemigo = enemigo.vidas
        self.puntuacion = self.jugador.puntuacion + self.tiempo_restante * 100 + self.jugador.vidas * 100 - 2
        texto_puntuacion = self.fuente_texto.render(f"PUNTUACION: {self.jugador.puntuacion}", True, "white")
        texto_tiempo_restante = self.fuente_texto.render(f"TIEMPO RESTANTE: {self.tiempo_restante:.0f}", True, "white")
        texto_vidas = self.fuente_texto.render(f"VIDAS: {self.jugador.vidas}", True, "white")
        texto_balas = self.fuente_texto.render(f"BALAS: {self.jugador.cantidad_proyectiles}", True, "white")
        self.tiempo_restante -= self.fps / 1000
        self._slave.blit(texto_puntuacion, (self.lista_tamaños[0] - 480, 25, self.lista_tamaños[0], 64))
        self._slave.blit(texto_vidas, (25, 25, self.lista_tamaños[0], 64))
        self._slave.blit(texto_balas, (25 + texto_vidas.get_width() + 15, 25, self.lista_tamaños[0], 64))
        self._slave.blit(texto_tiempo_restante, (self.lista_tamaños[0]//2 - 240, 25, self.lista_tamaños[0], 64))
    
    
