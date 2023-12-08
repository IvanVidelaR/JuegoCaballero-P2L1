import pygame, json
from pygame.locals import *

from Gui.GUI_button import *
#No se instancia. Es la base de la jerarquia

class Form(Widget):
    def __init__(self, screen, x,y,w,h,color_background,color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h, color_background, color_border, border_size)
        self._slave = pygame.Surface((w,h))
        self.slave_rect = self._slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.lista_widgets = []
        self.hijo = None
        self.dialog_result = None
        self.padre = None
        self.flag_play = True
        
        self.volumen_musica, self.volumen_efectos = self.cargar_configuracion()
    
    def show_dialog(self, formulario):
        self.hijo = formulario
        self.hijo.padre = self

    def end_dialog(self):
        self.dialog_result = "OK"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo == None or self.hijo.dialog_result != None

    def render(self):
        pass

    def update(self, lista_eventos):
        pass
    
    def cargar_configuracion(self):
        try:
            with open(r"src\Assets\archives\configuracion.txt", "r") as archivo:
                for linea in archivo.readlines():
                    if linea.startswith("musica"):
                        self.volumen_musica = int(linea.split(":")[1])
                    if linea.startswith("efectos"):
                        self.volumen_efectos = int(linea.split(":")[1])
        except FileNotFoundError:
            self.volumen_musica = 2
            self.volumen_efectos = 2

        return self.volumen_musica, self.volumen_efectos
    
    def guardar_configuracion(self):
        with open(r"src\Assets\archives\configuracion.txt", "w") as archivo:
            archivo.write("musica:{}\nefectos:{}".format(self.volumen_musica, self.volumen_efectos))

    def guardar_niveles(self, nivel_a_guardar):
        data = {"nivel": nivel_a_guardar}
        with open(r"src\Assets\archives\nivel.json", "w") as archivo:
            json.dump(data, archivo)

    def cargar_niveles(self):
        try:
            with open(r"src\Assets\archives\nivel.json", "r") as archivo:
                data = json.load(archivo)
                nivel = data["nivel"]
        except FileNotFoundError:
            nivel = 0

        return nivel
