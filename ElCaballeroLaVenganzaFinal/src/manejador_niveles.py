from pygame.locals import *
from class_nivel_uno import *
from class_nivel_dos import *
from class_nivel_tres import *

class Manejador_niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}

    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)