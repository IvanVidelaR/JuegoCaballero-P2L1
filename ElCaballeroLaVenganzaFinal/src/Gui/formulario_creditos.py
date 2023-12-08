from Gui.formulario_configuracion import *

class FormCreditos(Form):
    def __init__(self, screen, x, y, w, h, active, path_image):
        super().__init__(screen, x, y, w, h, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image
        self.screen = screen

        self.btn_home = Button_Image(self._slave, x, y, x+200, y-140, 50, 50, r"src\Assets\images\GUI\buttons\button_home.png", self.btn_home_click, "lalal")
        lbl_creditos_titulo = Label(self._slave, x - 100, y - 180, 200, 100, "Créditos", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")
        lbl_creditos_tabla = Label(self._slave, x - 223, y - 85, 445, 240, "Iván Agustín Videla Ribodino", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\tabla-creditos.png")

        self.lista_widgets.append(lbl_creditos_titulo)
        self.lista_widgets.append(lbl_creditos_tabla)
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

