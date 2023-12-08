import pygame, sys
import sqlite3
from pygame.locals import *

from Gui.GUI_button import * #caja donde se pausa y continua el juego
from Gui.GUI_slider import * #caja donde se sube y baja el volumen
from Gui.GUI_textbox import * #caja donde se escribe el nombre
from Gui.GUI_label import * #caja donde muestra el porcentaje de volumen
from Gui.GUI_form import * #caja formulario principal
from Gui.GUI_button_image import * #caja imagen
from Gui.formulario_ranking import * 
from Gui.formulario_seleccion_nivel import * 
from Gui.formulario_configuracion import *
from Gui.formulario_instrucciones import *
from Gui.formulario_creditos import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image
        self.screen = screen

        self.btn_ranking = Button_Image(self._slave, x, y, x+200, y+95, 50, 50, r"src\Assets\images\GUI\buttons\button_ranking.png", self.btn_ranking_click, "lalal")
        self.btn_instrucciones = Button_Image(self._slave, x, y, x -258, y+98, 50, 50, r"src\Assets\images\GUI\buttons\button_instrucciones.png", self.btn_instrucciones_click, "lalal")
        self.btn_jugar = Button_Image(self._slave, x, y, x//2 + 30, y//2 +20, 260, 50, "src\Assets\images\GUI\play.png", self.btn_jugar_click, "lalal")
        self.btn_settings = Button_Image(self._slave, x, y, x//2 + 30, y//2 + 80, 260, 50, "src\Assets\images\GUI\settings.png", self.btn_settings_click, "lalal")
        self.btn_exit = Button_Image(self._slave, x, y, x//2 + 30, y//2 + 140, 260, 50, "src\Assets\images\GUI\credits.png", self.btn_exit_click, "lalal")
        lbl_menu = Label(self._slave, x - 100, y - 180, 200, 100, "Menu", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")
        
        self.lista_widgets.append(self.btn_ranking)
        self.lista_widgets.append(self.btn_instrucciones)
        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_exit)
        self.lista_widgets.append(self.btn_settings)
        self.lista_widgets.append(lbl_menu)

        pygame.mixer.init()
        
        pygame.mixer.music.load("src\Assets\sounds\Fate.wav")
        pygame.mixer.music.set_volume(self.volumen_musica / 10)
        pygame.mixer.music.play(-1)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
                # self.render()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            # self.update_volumen(lista_eventos)
            FONDO = pygame.image.load(r"src\Assets\images\GUI\fondo_menu.png")
            FONDO = pygame.transform.scale(FONDO, (1280, 720))
            self.screen.blit(FONDO, (0,0))
            #self.screen.fill("Black")
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_exit_click(self, texto):
        form_creditos = FormCreditos(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png")
        self.show_dialog(form_creditos)
    
    def btn_settings_click(self, texto):
        form_configuracion = FormConfiguracion(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png")
        self.show_dialog(form_configuracion)

    def btn_ranking_click(self, texto):
        dic_score = self.extraer_ranking()
        
        form_puntaje = FormMenuScore(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png", dic_score)

        self.show_dialog(form_puntaje)
    
    def btn_instrucciones_click(self, texto):
        form_instrucciones = FormInstrucciones(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png")
        self.show_dialog(form_instrucciones)

    def btn_jugar_click(self, texto):
        formulario_jugar = FormMenuPlay(self._master, 400, 100, 498.5, 553, True, r"src\Assets\images\GUI\tabla.png")

        self.show_dialog(formulario_jugar)
    
    def extraer_ranking(self):
        with sqlite3.connect(r"src\Assets\archives\base_de_datos.db") as conexion:
            try:
                dic_score = []
                sentencia = '''
                            select * from Jugadores order by puntuacion desc limit 3
                            '''
                cursor = conexion.execute(sentencia)
                for fila in cursor:
                    jugador = fila[1]
                    puntuacion = fila[2]
                    nivel = fila[3]
                    dic_score.append({"Jugador": jugador, "Score": puntuacion, "Nivel": nivel})
                
                print("Datos seleccionados con exito")
                return dic_score
            except:
                print("Error!!!")
        