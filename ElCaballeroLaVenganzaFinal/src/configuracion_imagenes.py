import pygame

def cargar_imagen(ruta):
    try:
        imagen = pygame.image.load(ruta)
        return imagen
    except Exception:
        # Manejo del error de lectura de la imagen
        print("Error al cargar la imagen:", ruta)
        raise SystemExit  # Salir del programa
    
def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []

    for imagen in lista_original:
        imagen = pygame.transform.flip(imagen, flip_x, flip_y)
        lista_girada.append(imagen)

    return lista_girada

personaje_quieto_derecha = [cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\0.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\1.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\2.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\3.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\4.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\5.png"),
                            #cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\6.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\7.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\8.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\9.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\10.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\11.png"),
                            #cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\12.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\13.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\14.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\15.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\16.png"),
                            #cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\17.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\18.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\19.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Quieto\20.png"),]

personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)

personaje_saltando_derecha = [cargar_imagen(r"src\Assets\images\caballero_principal\Salto\0.png")]

personaje_saltando_izquierda = girar_imagenes(personaje_saltando_derecha, True, False)

personaje_saltando_doble_derecha = [cargar_imagen(r"src\Assets\images\caballero_principal\Doble_salto\0.png"),
                                    cargar_imagen(r"src\Assets\images\caballero_principal\Doble_salto\1.png"),
                                    cargar_imagen(r"src\Assets\images\caballero_principal\Doble_salto\2.png"),
                                    cargar_imagen(r"src\Assets\images\caballero_principal\Doble_salto\3.png"),
                                    cargar_imagen(r"src\Assets\images\caballero_principal\Doble_salto\4.png"),
                                    cargar_imagen(r"src\Assets\images\caballero_principal\Doble_salto\5.png")]

personaje_saltando_doble_izquierda = girar_imagenes(personaje_saltando_doble_derecha, True, False)

personaje_corriendo_derecha = [cargar_imagen(r"src\Assets\images\caballero_principal\Correr\0.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\1.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\2.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\3.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\4.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\5.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\6.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\7.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\8.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\9.png"),
                                cargar_imagen(r"src\Assets\images\caballero_principal\Correr\10.png")]

personaje_corriendo_izquierda = girar_imagenes(personaje_corriendo_derecha, True, False)

personaje_cayendo_derecha = [cargar_imagen(r"src\Assets\images\caballero_principal\Caer\0.png")]

personaje_cayendo_izquierda = girar_imagenes(personaje_cayendo_derecha, True, False)

personaje_recibiendo_daño_derecha = [cargar_imagen(r"src\Assets\images\caballero_principal\Recibir_daño\0.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Recibir_daño\1.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Recibir_daño\2.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Recibir_daño\3.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Recibir_daño\4.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Recibir_daño\5.png"),
                            cargar_imagen(r"src\Assets\images\caballero_principal\Recibir_daño\6.png")]

personaje_recibiendo_daño_izquierda = girar_imagenes(personaje_recibiendo_daño_derecha, True, False)

plataforma_delgada = [cargar_imagen(r"src\Assets\images\plataformas\castillo\0.png")]
plataforma_llena = [cargar_imagen(r"src\Assets\images\plataformas\castillo\1.png")]
plataforma_super_delgada = [cargar_imagen(r"src\Assets\images\plataformas\castillo\2.png")]
plataforma_pared = [cargar_imagen(r"src\Assets\images\plataformas\castillo\3.png")]
plataforma_techo = [cargar_imagen(r"src\Assets\images\plataformas\castillo\4.png")]
plataforma_puerta_enemigos = [cargar_imagen(r"src\Assets\images\plataformas\castillo\5.png")]

plataforma_delgada_bosque = [cargar_imagen(r"src\Assets\images\plataformas\bosque\0.png")]
plataforma_llena_bosque = [cargar_imagen(r"src\Assets\images\plataformas\bosque\1.png")]
plataforma_super_delgada_bosque = [cargar_imagen(r"src\Assets\images\plataformas\bosque\2.png")]
plataforma_pared_bosque = [cargar_imagen(r"src\Assets\images\plataformas\bosque\3.png")]
plataforma_techo_bosque = [cargar_imagen(r"src\Assets\images\plataformas\bosque\4.png")]

bolsas_oro = [cargar_imagen(r"src\Assets\images\items\Bolsas_oro\0.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\1.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\2.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\3.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\4.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\5.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\6.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\7.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\8.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\9.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\10.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\11.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\12.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\13.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\14.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\15.png"),
            cargar_imagen(r"src\Assets\images\items\Bolsas_oro\16.png"),]

espada_proyectil = [cargar_imagen(r"src\Assets\images\items\Espada_proyectil\0.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\1.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\2.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\3.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\4.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\5.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\6.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\7.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\8.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\9.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\10.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\11.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\12.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\13.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\14.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\15.png"),
                    cargar_imagen(r"src\Assets\images\items\Espada_proyectil\16.png"),]

caliz_vino = [cargar_imagen(r"src\Assets\images\items\Caliz_vino\0.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\1.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\2.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\3.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\4.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\5.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\6.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\7.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\8.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\9.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\10.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\11.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\12.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\13.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\14.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\15.png"),
            cargar_imagen(r"src\Assets\images\items\Caliz_vino\16.png"),]

proyectil_derecha = [cargar_imagen(r"src\Assets\images\proyectil\0.png")]

proyectil_izquierda = girar_imagenes(proyectil_derecha, True, False)

pinchos = [cargar_imagen(r"src\Assets\images\trampas\Pinchos\0.png")]

sierras = [
            cargar_imagen(r"src\Assets\images\trampas\Sierras\0.png"),
            cargar_imagen(r"src\Assets\images\trampas\Sierras\1.png"),
            cargar_imagen(r"src\Assets\images\trampas\Sierras\2.png"),
            cargar_imagen(r"src\Assets\images\trampas\Sierras\3.png"),
            cargar_imagen(r"src\Assets\images\trampas\Sierras\4.png"),
            cargar_imagen(r"src\Assets\images\trampas\Sierras\5.png"),
            cargar_imagen(r"src\Assets\images\trampas\Sierras\6.png"),
            cargar_imagen(r"src\Assets\images\trampas\Sierras\7.png"),
            ]

duende_corriendo_derecha = [
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\0.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\1.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\2.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\3.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\4.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\5.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\6.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\7.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\8.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\9.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\10.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Correr\11.png"),
                            ]

duende_corriendo_izquierda = girar_imagenes(duende_corriendo_derecha, True, False)

esqueleto_corriendo_derecha = [
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\0.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\1.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\2.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\3.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\4.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\5.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\6.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\7.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\8.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\9.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\10.png"),
                                cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Correr\11.png"),
                            ]

esqueleto_corriendo_izquierda = girar_imagenes(esqueleto_corriendo_derecha, True, False)

caballero_malvado_corriendo_derecha = [
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\0.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\1.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\2.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\3.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\4.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\5.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\6.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\7.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\8.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\9.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\10.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Correr\11.png"),
                                        ]

caballero_malvado_corriendo_izquierda = girar_imagenes(caballero_malvado_corriendo_derecha, True, False)

duende_cayendo_derecha = [cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Caer\0.png")]

duende_cayendo_izquierda = girar_imagenes(duende_cayendo_derecha, True, False)

esqueleto_cayendo_derecha = [cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Caer\0.png")]

esqueleto_cayendo_izquierda = girar_imagenes(esqueleto_cayendo_derecha, True, False)

caballero_malvado_cayendo_derecha = [cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Caer\0.png")]

caballero_malvado_cayendo_izquierda = girar_imagenes(caballero_malvado_cayendo_derecha, True, False)

duende_recibiendo_daño_derecha = [
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Recibir_daño\0.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Recibir_daño\1.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Recibir_daño\2.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Recibir_daño\3.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Recibir_daño\4.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Recibir_daño\5.png"),
                            cargar_imagen(r"src\Assets\images\personajes_enemigos\duende\Recibir_daño\6.png"),
                        ]

duende_recibiendo_daño_izquierda = girar_imagenes(duende_recibiendo_daño_derecha, True, False)

esqueleto_recibiendo_daño_derecha = [
                                    cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Recibir_daño\0.png"),
                                    cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Recibir_daño\1.png"),
                                    cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Recibir_daño\2.png"),
                                    cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Recibir_daño\3.png"),
                                    cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Recibir_daño\4.png"),
                                    cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Recibir_daño\5.png"),
                                    cargar_imagen(r"src\Assets\images\personajes_enemigos\esqueleto\Recibir_daño\6.png"),
                                    
                                    ]

esqueleto_recibiendo_daño_izquierda = girar_imagenes(esqueleto_recibiendo_daño_derecha, True, False)

caballero_malvado_recibiendo_daño_derecha = [
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Recibir_daño\0.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Recibir_daño\1.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Recibir_daño\2.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Recibir_daño\3.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Recibir_daño\4.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Recibir_daño\5.png"),
                                        cargar_imagen(r"src\Assets\images\personajes_enemigos\caballero_malvado\Recibir_daño\6.png"),
                                            ]

caballero_malvado_recibiendo_daño_izquierda = girar_imagenes(caballero_malvado_recibiendo_daño_derecha, True, False)

caja_quieto = [cargar_imagen(r"src\Assets\images\caja\Quieto\0.png")]

caja_recibiendo_daño = [cargar_imagen(r"src\Assets\images\caja\Recibir_daño\0.png"),
                        cargar_imagen(r"src\Assets\images\caja\Recibir_daño\1.png"),
                        cargar_imagen(r"src\Assets\images\caja\Recibir_daño\2.png"),]