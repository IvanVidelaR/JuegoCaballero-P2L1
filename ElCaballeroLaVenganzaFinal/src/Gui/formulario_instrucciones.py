from Gui.formulario_configuracion import *

class FormInstrucciones(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image
        self.screen = screen

        self.btn_home = Button_Image(self._slave, x, y, x+200, y+95, 50, 50, r"src\Assets\images\GUI\buttons\button_home.png", self.btn_home_click, "lalal")
        lbl_instrucciones_titulo = Label(self._slave, x - 100, y - 180, 200, 100, "Instrucciones", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")
        pic_instrucciones_imagen = PictureBox(self._slave, x - 250, y - 110, 500, 250, r"src\Assets\images\GUI\instrucciones.png")
        self.lista_widgets.append(lbl_instrucciones_titulo)
        self.lista_widgets.append(pic_instrucciones_imagen)
        self.lista_widgets.append(self.btn_home)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def btn_home_click(self, param):
        self.end_dialog()

