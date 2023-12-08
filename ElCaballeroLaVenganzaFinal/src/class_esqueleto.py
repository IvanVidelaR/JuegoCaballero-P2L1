from class_personaje_enemigo import *

class Esqueleto(Personaje_enemigo):
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, animaciones: dict, tipo_animacion: str) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, tipo_animacion)
        self.cantidad_proyectiles = 60
        self.segundos_entre_disparo = 5
        self.que_es = "Esqueleto"

    def actualizar(self, pantalla, fps, lista_plataformas, jugador, diccionario_items_juego):
        super().actualizar(pantalla, fps, lista_plataformas, jugador)
        self.manejar_tiempo_disparo(fps)
        self.verificar_colision_proyectil(jugador)
        if self.disparo == False:
            self.lanzar_proyectil(diccionario_items_juego)
            self.disparo = True