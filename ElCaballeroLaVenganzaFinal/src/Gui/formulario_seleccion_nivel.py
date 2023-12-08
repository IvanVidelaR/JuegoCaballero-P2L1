import pygame
from pygame.locals import *

from Gui.formulario_juego import *
from manejador_niveles import *

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)
        self._x = x
        self._y = y
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image
        self.screen = screen

        nivel = self.cargar_niveles()
        self._btn_level_1 = Button_Image(screen = self._slave, x = 100, y = 100, master_x = x, master_y = y, w = 142.2, h = 131.8, onclick = self.entrar_nivel, onclick_param = "nivel_uno", path_image = r"src\Assets\images\GUI\lvl_1_select.png")
        if nivel == 1 or nivel == 2 or nivel == 3:
            self._btn_level_2 = Button_Image(screen = self._slave, x = 260, y = 113, master_x = x, master_y = y, w = 142.4, h = 121, onclick = self.entrar_nivel, onclick_param = "nivel_dos", path_image= r"src\Assets\images\GUI\lvl_2_select.png")
        else:
            self._btn_level_2 = Button_Image(screen = self._slave, x = 260, y = 113, master_x = x, master_y = y, w = 142.4, h = 121, onclick = self.entrar_nivel, onclick_param = "nivel_dos", path_image= r"src\Assets\images\GUI\lvl_2_blocked.png")
        if nivel == 2 or nivel == 3:
            self._btn_level_3 = Button_Image(screen = self._slave, x = 100, y = 250, master_x = x, master_y = y, w = 142.2, h = 121.2,  onclick = self.entrar_nivel, onclick_param = "nivel_tres", path_image= r"src\Assets\images\GUI\lvl_3_select.png")
        else:
            self._btn_level_3 = Button_Image(screen = self._slave, x = 100, y = 250, master_x = x, master_y = y, w = 142.2, h = 121.2,  onclick = self.entrar_nivel, onclick_param = "nivel_tres", path_image= r"src\Assets\images\GUI\lvl_3_blocked.png")

        self._btn_home = Button_Image(screen = self._slave, x = 390, y = 450, master_x = x, master_y = y, w = 50, h = 50, onclick = self.btn_home_click, onclick_param = "", path_image= r"src\Assets\images\GUI\buttons\button_home.png")

        lbl_seleccion_nivel = Label(self._slave, x - 280, y - 100, 250, 100, "Seleccionar nivel", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")

        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(lbl_seleccion_nivel)

    def on(self,parametro):
        print("hola", parametro)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            FONDO = pygame.image.load(r"src\Assets\images\GUI\fondo_menu.jpg")
            FONDO = pygame.transform.scale(FONDO, (1280, 720))
            self.update_niveles()
            self.screen.blit(FONDO, (0,0))
            #self.screen.fill("Black")
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def update_niveles(self):
        nivel = self.cargar_niveles()
        if nivel == 1 or nivel == 2 or nivel == 3:
            self._btn_level_2.aux_image = pygame.image.load(r"src\Assets\images\GUI\lvl_2_select.png")
            self._btn_level_2.aux_image = pygame.transform.scale(self._btn_level_2.aux_image,(142.4,121))
            self._btn_level_2._slave = self._btn_level_2.aux_image
        if nivel == 2 or nivel == 3:
            self._btn_level_3.aux_image = pygame.image.load(r"src\Assets\images\GUI\lvl_3_select.png")
            self._btn_level_3.aux_image = pygame.transform.scale(self._btn_level_3.aux_image,(142.2,121.2))
            self._btn_level_3._slave = self._btn_level_3.aux_image
            
    def entrar_nivel(self, nombre_nivel):
        nivel = self.cargar_niveles()
        if nombre_nivel == "nivel_dos":
            if nivel == 1 or nivel == 2 or nivel == 3:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel)
                self.show_dialog(form_contenedor_nivel)
        elif nombre_nivel == "nivel_tres":
            if nivel == 2 or nivel == 3:
                nivel = self.manejador_niveles.get_nivel(nombre_nivel)
                form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel)
                self.show_dialog(form_contenedor_nivel)
        else:
            nivel = self.manejador_niveles.get_nivel(nombre_nivel)
            form_contenedor_nivel = FormContenedorNivel(self._master, nivel, nombre_nivel)
            self.show_dialog(form_contenedor_nivel)
        
    def btn_home_click(self,param):
        self.end_dialog()