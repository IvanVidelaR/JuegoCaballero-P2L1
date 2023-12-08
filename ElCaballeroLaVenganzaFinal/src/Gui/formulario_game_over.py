from Gui.formulario_configuracion import *

class FormGameOver(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image
        self.screen = screen

        self.btn_play = Button_Image(self._slave,x, y, x - 140, y//2 + 30, 150, 150, r"src\Assets\images\GUI\buttons\button_restart.png", self.btn_play_click, "lalal")
        self.btn_settings = Button_Image(self._slave,x, y, x + 30, y//2 + 70, 100, 100, r"src\Assets\images\GUI\buttons\button_settings.png", self.btn_settings_click, "lalal")
        lbl_game_over = Label(self._slave, x - 100, y - 180, 200, 100, "Perdiste", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")
    
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_settings)
        self.lista_widgets.append(lbl_game_over)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def btn_play_click(self, param):
        self.end_dialog()

    def btn_settings_click(self, param):
        form_configuracion = FormConfiguracion(self._master, 320, 180, 640, 360, True, r"src\Assets\images\GUI\tabla.png")
        self.show_dialog(form_configuracion)
    
    
    