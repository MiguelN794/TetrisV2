import pygame
import constantes as c

class Tablero:
    def __init__(self, altura=18, ancho=10):
        self.altura = altura
        self.ancho = ancho
        self.tablero = self.crear_tablero()
        self.colores = self.crear_tablero()  # Matriz para almacenar los colores

    def crear_tablero(self):
        return [[0 for _ in range(self.ancho)] for _ in range(self.altura)]

    def imprimir_tablero(self):
        for fila in self.tablero:
            print(fila)

    def colocar_pieza(self, pieza):
        for i, fila in enumerate(pieza.forma):
            for j, valor in enumerate(fila):
                if valor:
                    self.tablero[pieza.posicion[0] + i][pieza.posicion[1] + j] = valor
                    self.colores[pieza.posicion[0] + i][pieza.posicion[1] + j] = pieza.color  # Almacenar el color

    def mover_pieza(self, pieza, direccion):
        # Direcciones: 'izquierda', 'derecha', 'abajo'
        if direccion == 'izquierda':
            pieza.posicion[1] -= 1
        elif direccion == 'derecha':
            pieza.posicion[1] += 1
        elif direccion == 'abajo':
            pieza.posicion[0] += 1

    def mover_pieza_al_fondo(self, pieza):
        while not self.detectar_colision(pieza):
            pieza.posicion[0] += 1
        pieza.posicion[0] -= 1
        self.colocar_pieza(pieza)


    def detectar_colision(self, pieza):
        for i, fila in enumerate(pieza.forma):
            for j, valor in enumerate(fila):
                if valor:
                    if (pieza.posicion[0] + i >= self.altura or
                        pieza.posicion[1] + j < 0 or
                        pieza.posicion[1] + j >= self.ancho or
                        self.tablero[pieza.posicion[0] + i][pieza.posicion[1] + j]):
                        return True
        return False

    def eliminar_filas_completas(self):
        filas_eliminadas = 0
        for i in range(self.altura):
            if 0 not in self.tablero[i]:
                del self.tablero[i]
                self.tablero.insert(0, [0 for _ in range(self.ancho)])
                filas_eliminadas += 1
        return filas_eliminadas

    def dibujar_cuadricula(self, pantalla, color, tamano_bloque):
        for i in range(self.altura):
            for j in range(self.ancho):
                x = c.TABLERO_X + j * tamano_bloque
                y = c.TABLERO_Y + i * tamano_bloque
                pygame.draw.rect(pantalla, color, (x, y, tamano_bloque, tamano_bloque), 1)

# Ejemplo de uso
if __name__ == "__main__":
    from pieza import Pieza, PIEZAS

    tablero = Tablero()
    pieza = Pieza(PIEZAS['T'])

    print("Tablero inicial:")
    tablero.imprimir_tablero()

    tablero.colocar_pieza(pieza)
    print("\nTablero con pieza T:")
    tablero.imprimir_tablero()

    tablero.mover_pieza(pieza, 'abajo')
    if not tablero.detectar_colision(pieza):
        tablero.colocar_pieza(pieza)
    print("\nTablero después de mover pieza T hacia abajo:")
    tablero.imprimir_tablero()

    # Simular una fila completa para probar la eliminación
    tablero.tablero[17] = [1] * 10
    print("\nTablero con una fila completa:")
    tablero.imprimir_tablero()

    filas_eliminadas = tablero.eliminar_filas_completas()
    print(f"\nTablero después de eliminar filas completas (filas eliminadas: {filas_eliminadas}):")
    tablero.imprimir_tablero()
