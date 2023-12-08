from Gui.GUI_form import *
from Gui.GUI_button_image import *
from Gui.GUI_label import *
from Gui.GUI_slider import *
from Gui.GUI_checkbox import *
from Gui.GUI_picture_box import *
from class_recompensa import *

class FormConfiguracion(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)
        
        self.screen = screen
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image

        self.flag_music = False

        lbl_musica = Label(self._slave, x - 75, 105, 150, 50, text="Música:", font="Verdana", font_size=15, font_color="White", path_image=r"src\Assets\images\GUI\barra_puntaje_titulo.png")
        self.barra_volumen = PictureBox(self._slave, x - 200, y - 20, 400, 50, r"src\Assets\images\GUI\barra_volumen_1.png")
        self.btn_bajar_volumen_musica = Button_Image(self._slave, x, y, x - 250, y - 20, 50, 50, r"src\Assets\images\GUI\buttons\button_back.png", self.btn_bajar_volumen_musica_click, "lalal")
        self.btn_subir_volumen_musica = Button_Image(self._slave, x, y, x + 200, y - 20, 50, 50, r"src\Assets\images\GUI\buttons\button_next.png", self.btn_subir_volumen_musica_click, "lalal")

        lbl_efectos = Label(self._slave, x - 75, 215, 150, 50, text="Efectos:", font="Verdana", font_size=15, font_color="White", path_image=r"src\Assets\images\GUI\barra_puntaje_titulo.png")
        self.barra_volumen_efectos = PictureBox(self._slave, x - 200, y + 90, 400, 50, r"src\Assets\images\GUI\barra_volumen_1.png")
        self.btn_bajar_volumen_efectos = Button_Image(self._slave, x, y, x - 250, y + 90, 50, 50, r"src\Assets\images\GUI\buttons\button_back.png", self.btn_bajar_volumen_efectos_click, "lalal")
        self.btn_subir_volumen_efectos = Button_Image(self._slave, x, y, x + 200, y + 90, 50, 50, r"src\Assets\images\GUI\buttons\button_next.png", self.btn_subir_volumen_efectos_click, "lalal")

        self.btn_home = Button_Image(self._slave, x, y, 70, 40, 50, 50, r"src\Assets\images\GUI\buttons\button_home.png", self.btn_home_click, "lalal")
        self.btn_music = CheckBox(self._slave, x, y, x + 200, 40, 50, 50, r"src\Assets\images\GUI\buttons\button_no_sound.png", r"src\Assets\images\GUI\buttons\button_sound.png")
        #Button_Image(self._slave, x, y, x -250, y + 97, 50, 50, r"src\Assets\images\GUI\buttons\button_sound.png", self.btn_play_click, "lalal")
        lbl_configuracion = Label(self._slave, x - 100, y - 180, 200, 100, "Configuración", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")
        
        self.lista_widgets.append(self.barra_volumen)
        self.lista_widgets.append(self.btn_bajar_volumen_musica)
        self.lista_widgets.append(self.btn_subir_volumen_musica)
        self.lista_widgets.append(self.barra_volumen_efectos)
        self.lista_widgets.append(self.btn_bajar_volumen_efectos)
        self.lista_widgets.append(self.btn_subir_volumen_efectos)
        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.btn_music)
        self.lista_widgets.append(lbl_musica)
        self.lista_widgets.append(lbl_efectos)
        self.lista_widgets.append(lbl_configuracion)

    def update(self, lista_eventos):
        self.draw()
        if self.verificar_dialog_result():
            self.draw()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.update_volumen_musica(lista_eventos)
            self.update_volumen_efectos(lista_eventos)
            self.btn_music_click()
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_music_click(self):
        if self.btn_music.get_esta_prendido():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        self.flag_music = not self.flag_music

    def btn_bajar_volumen_musica_click(self, param):
        if self.volumen_musica > 0:
            self.volumen_musica -= 2
    
    def btn_subir_volumen_musica_click(self, param):
        if self.volumen_musica < 10:
            self.volumen_musica += 2

    def btn_bajar_volumen_efectos_click(self, param):
        if self.volumen_efectos > 0:
            self.volumen_efectos -= 2
    
    def btn_subir_volumen_efectos_click(self, param):
        if self.volumen_efectos < 10:
            self.volumen_efectos += 2

    def update_volumen_musica(self, lista_eventos):
        pygame.mixer.music.set_volume(self.volumen_musica / 10)
        match(self.volumen_musica):
            case 0:
                self.barra_volumen.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_0.png")
                self.barra_volumen.aux_image = pygame.transform.scale(self.barra_volumen.aux_image,(400,50))
                self.barra_volumen._slave = self.barra_volumen.aux_image
            case 2:
                self.barra_volumen.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_1.png")
                self.barra_volumen.aux_image = pygame.transform.scale(self.barra_volumen.aux_image,(400,50))
                self.barra_volumen._slave = self.barra_volumen.aux_image
            case 4:
                self.barra_volumen.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_2.png")
                self.barra_volumen.aux_image = pygame.transform.scale(self.barra_volumen.aux_image,(400,50))
                self.barra_volumen._slave = self.barra_volumen.aux_image
            case 6:
                self.barra_volumen.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_3.png")
                self.barra_volumen.aux_image = pygame.transform.scale(self.barra_volumen.aux_image,(400,50))
                self.barra_volumen._slave = self.barra_volumen.aux_image
            case 8:
                self.barra_volumen.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_4.png")
                self.barra_volumen.aux_image = pygame.transform.scale(self.barra_volumen.aux_image,(400,50))
                self.barra_volumen._slave = self.barra_volumen.aux_image
            case 10:
                self.barra_volumen.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_5.png")
                self.barra_volumen.aux_image = pygame.transform.scale(self.barra_volumen.aux_image,(400,50))
                self.barra_volumen._slave = self.barra_volumen.aux_image

    def update_volumen_efectos(self, lista_eventos):
        match(self.volumen_efectos):
            case 0:
                self.barra_volumen_efectos.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_0.png")
                self.barra_volumen_efectos.aux_image = pygame.transform.scale(self.barra_volumen_efectos.aux_image,(400,50))
                self.barra_volumen_efectos._slave = self.barra_volumen_efectos.aux_image
            case 2:
                self.barra_volumen_efectos.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_1.png")
                self.barra_volumen_efectos.aux_image = pygame.transform.scale(self.barra_volumen_efectos.aux_image,(400,50))
                self.barra_volumen_efectos._slave = self.barra_volumen_efectos.aux_image
            case 4:
                self.barra_volumen_efectos.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_2.png")
                self.barra_volumen_efectos.aux_image = pygame.transform.scale(self.barra_volumen_efectos.aux_image,(400,50))
                self.barra_volumen_efectos._slave = self.barra_volumen_efectos.aux_image
            case 6:
                self.barra_volumen_efectos.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_3.png")
                self.barra_volumen_efectos.aux_image = pygame.transform.scale(self.barra_volumen_efectos.aux_image,(400,50))
                self.barra_volumen_efectos._slave = self.barra_volumen_efectos.aux_image
            case 8:
                self.barra_volumen_efectos.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_4.png")
                self.barra_volumen_efectos.aux_image = pygame.transform.scale(self.barra_volumen_efectos.aux_image,(400,50))
                self.barra_volumen_efectos._slave = self.barra_volumen_efectos.aux_image
            case 10:
                self.barra_volumen_efectos.aux_image = pygame.image.load(r"src\Assets\images\GUI\barra_volumen_5.png")
                self.barra_volumen_efectos.aux_image = pygame.transform.scale(self.barra_volumen_efectos.aux_image,(400,50))
                self.barra_volumen_efectos._slave = self.barra_volumen_efectos.aux_image

    def btn_home_click(self, param):
        self.guardar_configuracion()
        self.end_dialog()
