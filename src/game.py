import pygame
import sys
import random
import constantes as c
from pieza import Pieza, PIEZAS
from tablero import Tablero
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA, NEGRO, BLANCO, FPS, TAMANO_BLOQUE
from utils import rotar_matriz

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tetris by Alaceite")

# Configuración del reloj
reloj = pygame.time.Clock()

def dibujar_bloque(pantalla, x, y, color):
    # Dibuja un bloque individual con bordes y efecto 3D
    pygame.draw.rect(pantalla, color, (x, y, c.TAMANO_BLOQUE, c.TAMANO_BLOQUE), 0)

    # Borde claro (arriba e izquierda)
    pygame.draw.line(pantalla, (255, 255, 255), (x, y), (x + c.TAMANO_BLOQUE, y), 2)
    pygame.draw.line(pantalla, (255, 255, 255), (x, y), (x, y + c.TAMANO_BLOQUE), 2)

    # Borde oscuro (abajo y derecha)
    pygame.draw.line(pantalla, (100, 100, 100), (x, y + c.TAMANO_BLOQUE), (x + c.TAMANO_BLOQUE, y + c.TAMANO_BLOQUE), 2)
    pygame.draw.line(pantalla, (100, 100, 100), (x + c.TAMANO_BLOQUE, y), (x + c.TAMANO_BLOQUE, y + c.TAMANO_BLOQUE), 2)

def dibujar_marco(pantalla, x, y, ancho, alto, color, grosor):
    pygame.draw.rect(pantalla, color, (x, y, ancho, alto), grosor)

def dibujar_panel_pieza(pantalla, x, y, titulo, pieza=None):
    # Dibujar marco
    dibujar_marco(pantalla, x, y, c.CUADRO_LADO, c.CUADRO_LADO, c.GRIS_CLARO, c.GROSOR_MARCO)

    # Dibujar título
    fuente = pygame.font.Font(None, c.FUENTE_TITULO)
    texto = fuente.render(titulo, True, BLANCO)
    pantalla.blit(texto, (x + c.PADDING_MARCO, y - c.PADDING_MARCO))

    # Dibujar pieza si existe
    if pieza:
        centro_x = x + c.CUADRO_LADO // 2
        centro_y = y + c.CUADRO_LADO // 2
        for i, fila in enumerate(pieza.forma):
            for j, valor in enumerate(fila):
                if valor:
                    pos_x = centro_x + (j - len(pieza.forma[0])//2) * TAMANO_BLOQUE
                    pos_y = centro_y + (i - len(pieza.forma)//2) * TAMANO_BLOQUE
                    dibujar_bloque(pantalla, pos_x, pos_y, pieza.color)

def mostrar_puntuacion(pantalla, puntuacion):
    # Dibujar marco
    dibujar_marco(pantalla, c.SCORE_X, c.SCORE_Y, c.PANEL_LATERAL_ANCHO - c.MARGEN*2, 100, c.GRIS_CLARO, c.GROSOR_MARCO)

    # Dibujar título
    fuente_titulo = pygame.font.Font(None, c.FUENTE_TITULO)
    texto_titulo = fuente_titulo.render("SCORE", True, BLANCO)
    pantalla.blit(texto_titulo, (c.SCORE_X + c.PADDING_MARCO, c.SCORE_Y + c.PADDING_MARCO))

    # Dibujar puntuación
    fuente_score = pygame.font.Font(None, c.FUENTE_SCORE)
    texto_score = fuente_score.render(str(puntuacion), True, BLANCO)
    pantalla.blit(texto_score, (c.SCORE_X + c.PADDING_MARCO, c.SCORE_Y + c.PADDING_MARCO * 3))

def mostrar_pantalla_inicio(pantalla):
    pantalla.fill(NEGRO)
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render("TETRIS", True, BLANCO)
    pantalla.blit(texto, (ANCHO_PANTALLA // 2 - texto.get_width() // 2, ALTO_PANTALLA // 2 - texto.get_height() // 2))
    pygame.display.flip()
    esperar_tecla_inicio()

def mostrar_pantalla_final(pantalla):
    pantalla.fill(NEGRO)
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render("END", True, BLANCO)
    pantalla.blit(texto, (ANCHO_PANTALLA // 2 - texto.get_width() // 2, ALTO_PANTALLA // 2 - texto.get_height() // 2))
    pygame.display.flip()
    esperar_tecla_inicio()

def esperar_tecla_inicio():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                esperando = False

def dibujar_tablero(tablero):
    for i, fila in enumerate(tablero.tablero):
        for j, valor in enumerate(fila):
            if valor:
                color = tablero.colores[i][j]
                x = c.TABLERO_X + j * TAMANO_BLOQUE
                y = c.TABLERO_Y + i * TAMANO_BLOQUE
                dibujar_bloque(pantalla, x, y, color)
    tablero.dibujar_cuadricula(pantalla, (100, 100, 100), TAMANO_BLOQUE)


class Juego:
    def __init__(self):
        self.bolsa = list(PIEZAS.keys())
        random.shuffle(self.bolsa)
        self.siguiente_pieza = self.obtener_nueva_pieza()

    def obtener_nueva_pieza(self):
        if not self.bolsa:
            self.bolsa = list(PIEZAS.keys())
            random.shuffle(self.bolsa)
        pieza_clave = self.bolsa.pop()
        pieza_info = PIEZAS[pieza_clave]
        return Pieza(pieza_info['forma'], pieza_info['color'])

    def siguiente(self):
        self.siguiente_pieza = self.obtener_nueva_pieza()
        return self.siguiente_pieza


# Función principal del juego
def main():
    mostrar_pantalla_inicio(pantalla)
    tablero = Tablero()
    juego = Juego()
    pieza_actual = juego.siguiente()
    siguiente_pieza = juego.siguiente()
    pieza_almacenada = None
    puntuacion = 0
    contador_movimiento = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    pieza_actual.posicion[1] -= 1
                    if tablero.detectar_colision(pieza_actual):
                        pieza_actual.posicion[1] += 1
                elif evento.key == pygame.K_RIGHT:
                    pieza_actual.posicion[1] += 1
                    if tablero.detectar_colision(pieza_actual):
                        pieza_actual.posicion[1] -= 1
                elif evento.key == pygame.K_SPACE:  # Cambiar de K_DOWN a K_SPACE
                    tablero.mover_pieza_al_fondo(pieza_actual)
                    filas_eliminadas = tablero.eliminar_filas_completas()
                    puntuacion += filas_eliminadas * 100
                    pieza_actual = siguiente_pieza
                    siguiente_pieza = juego.siguiente()
                    if tablero.detectar_colision(pieza_actual):
                        print("Fin del juego")
                        pygame.quit()
                        sys.exit()
                elif evento.key == pygame.K_DOWN:
                            reloj.tick(c.FPS_DOWN)
                elif evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_DOWN:
                        reloj.tick(FPS)
                elif evento.key == pygame.K_UP:
                    pieza_actual.rotar()
                    if tablero.detectar_colision(pieza_actual):
                        pieza_actual.posicion[1] += 1
                        if tablero.detectar_colision(pieza_actual):
                            pieza_actual.posicion[1] -= 2
                            if tablero.detectar_colision(pieza_actual):
                                pieza_actual.posicion[1] += 1
                                pieza_actual.rotar()
                                pieza_actual.rotar()
                                pieza_actual.rotar()
                elif evento.key == pygame.K_LSHIFT:  # Almacenar o cambiar ficha con Shift izquierdo
                    if pieza_almacenada is None:
                        pieza_almacenada = pieza_actual
                        pieza_actual = siguiente_pieza
                        siguiente_pieza = juego.siguiente()
                    else:
                        pieza_almacenada, pieza_actual = pieza_actual, pieza_almacenada
                        pieza_almacenada.restablecer_posicion()
                    pieza_almacenada.posicion = [0, c.ANCHO_TABLERO // 2 - len(pieza_almacenada.forma[0]) // 2]
                    if tablero.detectar_colision(pieza_actual):
                        print("Fin del juego")
                        pygame.quit()
                        sys.exit()

        # Movimiento automático de la pieza hacia abajo
        contador_movimiento += 1
        if contador_movimiento >= 10:
            pieza_actual.posicion[0] += 1
            if tablero.detectar_colision(pieza_actual):
                pieza_actual.posicion[0] -= 1
                tablero.colocar_pieza(pieza_actual)
                filas_eliminadas = tablero.eliminar_filas_completas()
                puntuacion += filas_eliminadas * 100
                pieza_actual = siguiente_pieza
                siguiente_pieza = juego.siguiente()
                if tablero.detectar_colision(pieza_actual):
                    print("Fin del juego")
                    pygame.quit()
                    sys.exit()
            contador_movimiento = 0

        pantalla.fill(NEGRO)
        dibujar_tablero(tablero)
        for i, fila in enumerate(pieza_actual.forma):
            for j, valor in enumerate(fila):
                if valor:
                    x = c.TABLERO_X + (pieza_actual.posicion[1] + j) * TAMANO_BLOQUE
                    y = c.TABLERO_Y + (pieza_actual.posicion[0] + i) * TAMANO_BLOQUE
                    dibujar_bloque(pantalla, x, y, pieza_actual.color)

        # Dibujar paneles adicionales
        dibujar_panel_pieza(pantalla, c.NEXT_X, c.NEXT_Y, "NEXT", siguiente_pieza)
        dibujar_panel_pieza(pantalla, c.HOLD_X, c.HOLD_Y, "HOLD", pieza_almacenada)
        mostrar_puntuacion(pantalla, puntuacion)

        pygame.display.flip()
        reloj.tick(FPS)

if __name__ == "__main__":
    main()
