from Gui.GUI_textbox import *
from Gui.formulario_configuracion import *

import sqlite3

class FormVictoria(Form):
    def __init__(self, screen, x, y, w, h, active, path_image, puntuacion:int, nivel:str):
        super().__init__(screen, x, y, w, h, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w, h))
        self._slave = aux_image
        self.screen = screen
        self.puntuacion = puntuacion
        self.flag_save = False
        self._nivel = nivel

        self.btn_play = Button_Image(self._slave,x, y, x + 200, y + 95, 50, 50, r"src\Assets\images\GUI\buttons\button_home.png", self.btn_play_click, "lalal")
        self.btn_save = Button(self._slave, x, y, x//2 + 110, y//2 + 210, 100, 30, (100,31,0), "Black", self.btn_save_click, "Nombre", "Guardar", font="Verdana", font_size=15, font_color="Black")
        self.btn_settings = Button_Image(self._slave,x, y, x -250, y + 97, 50, 50, r"src\Assets\images\GUI\buttons\button_settings.png", self.btn_settings_click, "lalal")
        lbl_victoria = Label(self._slave, x - 100, y - 180, 200, 100, "Ganaste", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\titulos.png")
        lbl_puntuacion = Label(self._slave, x//2 -15, y//2 + 25, 350, 50, f"Puntos: {int(self.puntuacion)}", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\puntuaciones.png")
        lbl_nombre = Label(self._slave, x//2 -15, y//2 + 100, 350, 50, "Ingrese su nombre:", "Comic Sans", 30, (100,31,0), r"src\Assets\images\GUI\puntuaciones.png")
        self.txtbox = TextBox(self._slave, x, y, x//2, y//2 + 175, x, 30, "Gray", "White", (100,31,0), (65,120,3), 2, font = "Comic Sans", font_size = 15, font_color = "Black")

        self.lista_widgets.append(self.btn_save)
        self.lista_widgets.append(lbl_puntuacion)
        self.lista_widgets.append(lbl_nombre)
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_settings)
        self.lista_widgets.append(lbl_victoria)

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
    
    def btn_save_click(self, texto):
        if self.flag_save:
            nombre = self.txtbox.get_text()
            puntuacion = round(self.puntuacion)
            nivel = self._nivel
            self.crear_insertar_base_de_datos(nombre, puntuacion, nivel)
        else:
            self.btn_save._color_background = (100,31,0)
            self.btn_save._font_color = "Black"
            self.btn_save.set_text("Guardar")
    
        self.flag_save = not self.flag_save
    
    def crear_insertar_base_de_datos(self, nombre, puntuacion, nivel):
        with sqlite3.connect(r"src\Assets\archives\base_de_datos.db") as conexion:
                try:
                    # Crear una tabla si no existe
                    conexion.execute('''
                        CREATE TABLE IF NOT EXISTS Jugadores
                        (
                            id integer primary key autoincrement,
                            nombre text,
                            puntuacion integer,
                            nivel text
                        )
                    ''')

                    # Insertar los datos en la tabla
                    conexion.execute('INSERT INTO Jugadores (nombre, puntuacion, nivel) VALUES (?, ?, ?)', (nombre, puntuacion, nivel))

                    self.btn_save._color_background = (65,120,3)
                    self.btn_save._font_color = "Black"
                    self.btn_save.set_text("Guardado")
                    print("Datos insertados correctamente")
                except Exception:
                    print("Error al insertar los datos")

    