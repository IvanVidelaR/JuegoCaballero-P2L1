import pygame, sys
from pygame.locals import *
from class_nivel_uno import *
from class_nivel_dos import *
from class_nivel_tres import *
from Gui.GUI_form_principal import FormPrueba

#PANTALLA
ANCHO = 1280
ALTO = 720
FPS = 30
TAMAÑO_PANTALLA = (ANCHO, ALTO)

pygame.init()

PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
RELOJ = pygame.time.Clock()

form_prueba = FormPrueba(PANTALLA, ANCHO // 4, ALTO // 4, ANCHO // 2, ALTO // 2, True,  r"src\Assets\images\GUI\tabla.png")

pygame.display.set_caption("El Caballero: La Venganza Final")

while True:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    #PANTALLA.fill("Black")

    form_prueba.update(lista_eventos)

    pygame.display.flip()
