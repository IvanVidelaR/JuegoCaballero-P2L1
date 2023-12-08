import pygame

class Objeto_Juego():
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, animaciones:dict, tipo_animacion:str) -> None:
        #CONFECCIÓN
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_secuencias = 0
        self.animaciones = animaciones
        self.tipo_animacion = tipo_animacion
        self.reescalar_animaciones()
        imagen = self.animaciones[tipo_animacion][0]
        #RECTANGULOS
        self.rectangulo = imagen.get_rect()
        self.x_inicial = posicion_inicial[0]
        self.y_inicial = posicion_inicial[1]
        self.rectangulo.x = self.x_inicial
        self.rectangulo.y = self.y_inicial
        self.lados = self.obtener_rectangulos(self.rectangulo)
    
    def reescalar_imagen(self, lista_imagenes:list, tamaño:tuple):
        for i in range(len(lista_imagenes)):
            lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)
    
    def obtener_rectangulos(self, principal)->dict:            
        diccionario = {}

        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 20, principal.width, 20)
        diccionario["right"] = pygame.Rect(principal.right -10, principal.top, 10, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 15)

        return diccionario
    
    def reescalar_animaciones(self):
        if "plataforma" in self.tipo_animacion or "item" in self.tipo_animacion:
            for estado in self.animaciones:
                if estado == self.tipo_animacion:
                    self.reescalar_imagen(self.animaciones[estado], (self.ancho, self.alto))
        else:
            for estado in self.animaciones:
                self.reescalar_imagen(self.animaciones[estado], (self.ancho, self.alto))

    def dibujar_animacion(self, pantalla, tipo_animacion:str):
        animacion = self.animaciones[tipo_animacion]
        largo = len(animacion)
        
        if self.contador_secuencias >= largo:
            self.contador_secuencias = 0

        pantalla.blit(animacion[self.contador_secuencias], (self.rectangulo.x, self.rectangulo.y))
        
        self.contador_secuencias += 1

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad    
            
    def actualizar(self, pantalla):
        self.dibujar_animacion(pantalla, self.tipo_animacion)
