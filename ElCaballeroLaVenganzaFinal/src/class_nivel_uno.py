import pygame
from class_nivel import Nivel
from configuracion_imagenes import *
from class_personaje_principal import *
from class_personaje_enemigo import *
from class_plataforma import *
from class_items import *
from class_trampa import *
from class_proyectil import *
from class_recompensa import *

class NivelUno(Nivel):
    def __init__(self, pantalla):
        mundo = [
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        [2,9,6,0,0,0,0,0,0,0,0,0,0,0,0,0,7,9,6,2],
        [2,4,4,4,5,0,0,0,6,0,9,0,0,0,0,5,4,4,4,2],
        [2,10,0,0,0,0,0,11,0,7,0,0,0,0,0,0,0,0,10,2],
        [2,4,5,0,0,0,5,4,4,0,0,4,4,5,0,0,0,5,4,2],
        [2,0,0,0,0,0,0,11,0,6,0,11,0,0,6,0,0,0,0,2],
        [2,0,0,6,0,5,4,4,4,4,4,4,4,4,5,7,0,0,6,2],
        [2,11,0,0,7,0,0,0,9,0,0,0,0,6,0,9,0,11,10,2],
        [2,4,4,4,4,5,0,0,0,0,6,0,9,0,5,4,4,4,4,2],
        [2,0,6,0,9,0,0,0,5,4,4,5,7,0,0,0,0,9,0,2],
        [8,0,11,0,11,0,0,9,0,0,0,0,0,0,0,11,0,11,6,8],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
        ANCHO = pantalla.get_width()
        ALTO = pantalla.get_height()
        TAMAÑO_PANTALLA = (ANCHO, ALTO)
        FPS = 30
        FONDO = pygame.image.load(r"src\Assets\images\background\bosque.jpg")
        FONDO = pygame.transform.scale(FONDO, TAMAÑO_PANTALLA)
        FUENTE_TEXTO = pygame.font.Font(r"src\Assets\images\texto_fuente\PixelGameFont.ttf", 30)
        
        diccionario_animaciones = {}
        diccionario_animaciones["quieto_derecha"] = personaje_quieto_derecha
        diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
        diccionario_animaciones["saltar_derecha"] = personaje_saltando_derecha
        diccionario_animaciones["saltar_izquierda"] = personaje_saltando_izquierda
        diccionario_animaciones["correr_derecha"] = personaje_corriendo_derecha
        diccionario_animaciones["correr_izquierda"] = personaje_corriendo_izquierda
        diccionario_animaciones["caer_derecha"] = personaje_cayendo_derecha
        diccionario_animaciones["caer_izquierda"] = personaje_cayendo_izquierda
        diccionario_animaciones["saltar_doble_derecha"] = personaje_saltando_doble_derecha
        diccionario_animaciones["saltar_doble_izquierda"] = personaje_saltando_doble_izquierda
        diccionario_animaciones["recibir_daño_derecha"] = personaje_recibiendo_daño_derecha
        diccionario_animaciones["recibir_daño_izquierda"] = personaje_recibiendo_daño_izquierda

        diccionario_plataformas = {}
        diccionario_plataformas["plataforma_llena"] = plataforma_llena
        diccionario_plataformas["plataforma_delgada"] = plataforma_delgada
        diccionario_plataformas["plataforma_super_delgada"] = plataforma_super_delgada
        diccionario_plataformas["plataforma_pared"] = plataforma_pared
        diccionario_plataformas["plataforma_techo"] = plataforma_techo
        diccionario_plataformas["plataforma_puerta_enemigos"] = plataforma_puerta_enemigos

        diccionario_items_juego = {}
        diccionario_items_juego["bolsas_oro_item"] = bolsas_oro
        diccionario_items_juego["caliz_vino_item"] = caliz_vino
        diccionario_items_juego["espada_proyectil_item"] = espada_proyectil
        diccionario_items_juego["proyectil_derecha_item"] = proyectil_derecha
        diccionario_items_juego["proyectil_izquierda_item"] = proyectil_izquierda
        diccionario_items_juego["pinchos_item"] = pinchos

        diccionario_enemigo = {}
        diccionario_enemigo["correr_derecha"] = duende_corriendo_derecha
        diccionario_enemigo["correr_izquierda"] = duende_corriendo_izquierda
        diccionario_enemigo["caer_derecha"] = duende_cayendo_derecha
        diccionario_enemigo["caer_izquierda"] = duende_cayendo_izquierda
        diccionario_enemigo["recibir_daño_derecha"] = duende_recibiendo_daño_derecha
        diccionario_enemigo["recibir_daño_izquierda"] = duende_recibiendo_daño_izquierda
        
        diccionario_caja = {}
        diccionario_caja["caja_quieto"] = caja_quieto
        diccionario_caja["caja_recibir_daño"] = caja_recibiendo_daño

        TAMAÑO_BALDOSA_GRUESO = 64
        TAMAÑO_BALDOSA_DELGADO = 32
        TAMAÑO_BALDOSA_SUPER_DELGADO = 16

        lista_tamaños = [ANCHO, ALTO, TAMAÑO_BALDOSA_GRUESO]
        lista_plataformas = []
        lista_items = []
        lista_enemigos = self.generar_enemigo_aleatorio(ANCHO, diccionario_enemigo, 2)

        contador_filas = 0
        caballero = Personaje_principal((50,60), (64, ALTO - 128), diccionario_animaciones, "quieto_derecha")

        for fila in mundo:
            contador_columnas = 0
            for baldosa in fila:
                if baldosa == 1:
                    #PISO
                    lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_llena", True))
                if baldosa == 2:
                    #PAREDES
                    if contador_columnas == 0:
                       lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_DELGADO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_pared", True))
                    elif contador_columnas == len(fila) - 1:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_DELGADO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_pared", True))
                if baldosa == 3:
                    lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_techo", True))
                    if contador_columnas == 0:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_DELGADO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_pared", True))    
                    elif contador_columnas == len(fila) - 1:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_DELGADO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_pared", True))
                if baldosa == 4:
                    if contador_columnas > 9:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_DELGADO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_delgada", True))
                        if contador_columnas == 10:
                            lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_DELGADO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO - TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_delgada", True))
                    else:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_DELGADO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO - TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_delgada", True))
                if baldosa == 5:
                    if contador_columnas > 9:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_SUPER_DELGADO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_super_delgada", True))
                    else:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_SUPER_DELGADO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO - TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_super_delgada", True))
                if baldosa == 6:
                    lista_items.append(Recompensa((30, 29), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO), diccionario_items_juego, "bolsas_oro_item"))
                if baldosa == 7:
                    lista_enemigos.append(Personaje_enemigo((65,60), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_enemigo, "correr_derecha"))
                if baldosa == 8:
                    if contador_columnas == 0:
                       lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_SUPER_DELGADO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_SUPER_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_puerta_enemigos", True))
                    elif contador_columnas == len(fila) - 1:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_SUPER_DELGADO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_plataformas, "plataforma_puerta_enemigos", True))
                if baldosa == 9:
                    lista_items.append(Recompensa((15, 29), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_items_juego, "espada_proyectil_item"))
                if baldosa == 10:
                    if contador_columnas < 9:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO - TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_caja, "caja_quieto", False))
                        lista_items.append(Recompensa((30, 29), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO), diccionario_items_juego, "caliz_vino_item"))
                    else:
                        lista_plataformas.append(Plataforma((TAMAÑO_BALDOSA_GRUESO, TAMAÑO_BALDOSA_GRUESO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO, contador_filas * TAMAÑO_BALDOSA_GRUESO), diccionario_caja, "caja_quieto", False))
                        lista_items.append(Recompensa((30, 29), (contador_columnas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO), diccionario_items_juego, "caliz_vino_item"))
                if baldosa == 11:
                    lista_items.append(Trampa((TAMAÑO_BALDOSA_DELGADO, TAMAÑO_BALDOSA_SUPER_DELGADO), (contador_columnas * TAMAÑO_BALDOSA_GRUESO, contador_filas * TAMAÑO_BALDOSA_GRUESO + TAMAÑO_BALDOSA_DELGADO + TAMAÑO_BALDOSA_SUPER_DELGADO), diccionario_items_juego, "pinchos_item"))
                contador_columnas += 1
            contador_filas += 1


        super().__init__(pantalla, caballero, lista_plataformas, lista_items, lista_enemigos, FONDO, FPS, lista_tamaños, FUENTE_TEXTO, diccionario_items_juego)        

    def generar_enemigo_aleatorio(self, ancho_pantalla, diccionario_enemigos, cantidad_enemigos):
        lista_enemigos = []
        for i in range(cantidad_enemigos):
            x = random.randrange(400, ancho_pantalla - 400, 60)
            y = random.randrange(-500, 0, 60)
            nuevo_enemigo = Personaje_enemigo((65,60),(x, y), diccionario_enemigos, "correr_derecha")
            lista_enemigos.append(nuevo_enemigo)

        return lista_enemigos