import constantes as c

class Pieza:
    def __init__(self, forma, color):
        self.forma = forma
        self.color = color
        self.posicion = [0, 4]  # Posición inicial en el tablero (fila, columna)
        self.forma_inicial = [fila[:] for fila in forma]

    def rotar(self):
        # Rotar la pieza 90 grados en sentido horario
        self.forma = [list(reversed(col)) for col in zip(*self.forma)]

    def restablecer_posicion(self):
        self.forma = [fila[:] for fila in self.forma_inicial]

# Definición de las diferentes formas de piezas y sus colores
PIEZAS = {
    'I': {
        'forma': [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        'color': c.CYAN
    },
    'O': {
        'forma': [
            [1, 1],
            [1, 1]
        ],
        'color': c.AMARILLO
    },
    'T': {
        'forma': [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ],
        'color': c.MORADO
    },
    'S': {
        'forma': [
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]
        ],
        'color': c.VERDE
    },
    'Z': {
        'forma': [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]
        ],
        'color': c.ROJO
    },
    'J': {
        'forma': [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ],
        'color': c.AZUL
    },
    'L': {
        'forma': [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ],
        'color': c.NARANJA
    }
}

# Ejemplo de uso
if __name__ == "__main__":
    for nombre, datos in PIEZAS.items():
        pieza = Pieza(datos['forma'], datos['color'])
        print(f"Pieza {nombre} original:")
        for fila in pieza.forma:
            print(fila)

        pieza.rotar()
        print(f"\nPieza {nombre} rotada:")
        for fila in pieza.forma:
            print(fila)
        print("\n" + "-"*20 + "\n")
