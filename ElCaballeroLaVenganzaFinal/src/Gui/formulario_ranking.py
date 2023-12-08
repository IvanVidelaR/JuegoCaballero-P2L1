import pygame
from pygame.locals import *

from Gui.GUI_form import *
from Gui.GUI_label import *
from Gui.GUI_button_image import *

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, active, path_image, score):
        super().__init__(screen, x, y, w, h, active)

        aux_imagen = pygame.image.load(path_image)
        aux_imagen = pygame.transform.scale(aux_imagen, (w, h))

        self._slave = aux_imagen
        self._score = score
        self.screen = screen

        lbl_ranking = Label(self._slave, x - 100, y - 180, 200, 100, "Ranking", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")

        lbl_jugador = Label(self._slave, x - 250, 110, 150, 50, text="Jugador", font="Verdana", font_size=15, font_color="White", path_image=r"src\Assets\images\GUI\barra_puntaje_titulo.png")

        lbl_puntaje = Label(self._slave, x - 75, 110, 150, 50, text="Puntaje", font="Verdana", font_size=15, font_color="White", path_image=r"src\Assets\images\GUI\barra_puntaje_titulo.png")

        lbl_nivel = Label(self._slave, x + 100, 110, 150, 50, text="Nivel", font="Verdana", font_size=15, font_color="White", path_image=r"src\Assets\images\GUI\barra_puntaje_titulo.png")
        
        self._btn_home = Button_Image(screen = self._slave, x = 70, y = 40, master_x = x, master_y = y, w = 50, h = 50, onclick = self.btn_home_click, onclick_param = "", path_image= r"src\Assets\images\GUI\buttons\button_home.png")

        self.lista_widgets.append(lbl_ranking)
        self.lista_widgets.append(lbl_nivel)
        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_puntaje)
        self.lista_widgets.append(self._btn_home)

        pos_inicial_y = 160
        
        for j in self._score:
            pos_inicial_x = x - 250
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, 150, 50, cadena, "Verdana", 15, "White", r"src\Assets\images\GUI\barra_puntaje.png")
                self.lista_widgets.append(jugador)
                pos_inicial_x += 175
            pos_inicial_y += 50
        
    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            #self.screen.fill("Black")
            self.draw()
    
    def btn_home_click(self, param):
        self.end_dialog()


