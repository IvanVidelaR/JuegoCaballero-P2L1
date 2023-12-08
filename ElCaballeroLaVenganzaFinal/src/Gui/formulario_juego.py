import pygame
from pygame.locals import *

from Gui.formulario_pausa import *
from Gui.formulario_ranking import * 
from Gui.formulario_game_over import *
from Gui.formulario_victoria import *
from class_recompensa import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel, nombre_nivel:str):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), color_background="Black")
        nivel._slave = self._slave
        self._nivel = nivel
        self._nombre_nivel = nombre_nivel
        self._btn_home = Button_Image(screen = self._slave, master_x = self._x, master_y = self._y, x = self._w - 55, y = 10, w = 50, h = 50, onclick = self.btn_home_click, onclick_param = "", path_image= r"src\Assets\images\GUI\buttons\button_home.png")
        self._btn_pause = Button_Image(screen = self._slave, master_x = self._x, master_y = self._y, x = self._w - 110, y = 10, w = 50, h = 50, onclick = self.btn_pause_click, onclick_param = "", path_image= r"src\Assets\images\GUI\buttons\button_pause.png")
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_pause)
        
        self.nivel_perdido = False
        self.nivel_ganado = False

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            self._nivel.update(lista_eventos)
            self.update_efectos_juego(lista_eventos)
            self.cerrar_nivel_perder()
            self.cerrar_nivel_ganar()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_home_click(self, param):
        self.end_dialog()

    def btn_pause_click(self, param):
        form_pausa = FormPausa(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png")
        self.show_dialog(form_pausa)

    def cerrar_nivel_perder(self):
        if self._nivel.jugador.vidas <= 0 or (self._nombre_nivel == "nivel_tres" and self._nivel.tiempo_restante <= 0):
            if self.nivel_perdido:
                self.end_dialog()
            else:
                formulario_game_over = FormGameOver(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png")
                self.show_dialog(formulario_game_over)
                self.nivel_perdido = True

    def cerrar_nivel_ganar(self):

        if self._nombre_nivel == "nivel_uno" or self._nombre_nivel == "nivel_dos":
            if self._nivel.tiempo_restante <= 0:
                if self._nombre_nivel == "nivel_uno":
                    if self.cargar_configuracion != 1 or self.cargar_configuracion() != 2 or self.cargar_configuracion() != 3:
                        self.guardar_niveles(1)
                elif self._nombre_nivel == "nivel_dos":
                    if self.cargar_configuracion() != 2 or self.cargar_configuracion() != 3:
                        self.guardar_niveles(2)
                else:
                    self.guardar_niveles(3)
                puntuacion = self._nivel.puntuacion
                if self.nivel_ganado:
                    self.end_dialog()
                else:
                    formulario_victoria = FormVictoria(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png", puntuacion, self._nombre_nivel)
                    self.show_dialog(formulario_victoria)
                    self.nivel_ganado = True
        else:
            if self._nivel.vidas_enemigo <= 1:
                puntuacion = self._nivel.puntuacion
                if self.nivel_ganado:
                    self.end_dialog()
                else:
                    formulario_victoria = FormVictoria(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png", puntuacion, self._nombre_nivel)
                    self.show_dialog(formulario_victoria)
                    self.nivel_ganado = True

    def update_efectos_juego(self, lista_eventos):
        self.volumen_musica, self.volumen_efectos = self.cargar_configuracion()
        for item in self._nivel.items:
            if isinstance(item, Recompensa):
                item.sonido_bolsas_oro_item.set_volume(self.volumen_efectos / 10)
                item.sonido_caliz_vino_item.set_volume(self.volumen_efectos / 10)
                item.sonido_espada_proyectil_item.set_volume(self.volumen_efectos / 10)
        
        for enemigo in self._nivel.enemigos:
            enemigo.sonido_enemigo_puerta.set_volume(self.volumen_efectos / 10)
            enemigo.sonido_daño_duende.set_volume(self.volumen_efectos / 10)
            enemigo.sonido_daño_caballero_malvado.set_volume(self.volumen_efectos / 10)
            enemigo.sonido_daño_esqueleto.set_volume(self.volumen_efectos / 10)
            enemigo.sonido_lanzar_espada.set_volume(self.volumen_efectos / 10)
        
        self._nivel.jugador.sonido_pisando.set_volume(self.volumen_efectos / 10)
        self._nivel.jugador.sonido_daño_personaje_principal.set_volume(self.volumen_efectos / 10)
        self._nivel.jugador.sonido_lanzar_espada.set_volume(self.volumen_efectos / 10)

        for plataforma in self._nivel.plataformas:
            plataforma.sonido_impacto_plataforma.set_volume(self.volumen_efectos / 10)
            plataforma.sonido_impacto_caja.set_volume(self.volumen_efectos / 10)

    