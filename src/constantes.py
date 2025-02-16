# Dimensiones de la pantalla
ANCHO_PANTALLA = 750  # Aumentado para acomodar paneles
ALTO_PANTALLA = 600

# Dimensiones y posiciones de los paneles
MARGEN = 20
PANEL_LATERAL_ANCHO = 150

# Tamaño de cada bloque
TAMANO_BLOQUE = 30

#Panel izquierdo - Cuadros para piezas
CUADRO_LADO = 150  # Tamaño del cuadro contenedor

# Tablero principal
ANCHO_TABLERO = 10
ALTO_TABLERO = 18
TABLERO_X = (ANCHO_PANTALLA - (ANCHO_TABLERO * TAMANO_BLOQUE) - PANEL_LATERAL_ANCHO) // 2 + PANEL_LATERAL_ANCHO - 60
TABLERO_Y = MARGEN

# Panel izquierdo - Cuadros para piezas
NEXT_X = TABLERO_X - CUADRO_LADO - MARGEN
NEXT_Y = MARGEN
HOLD_X = NEXT_X
HOLD_Y = NEXT_Y + CUADRO_LADO + MARGEN

# Panel derecho - Puntuación
SCORE_X = TABLERO_X + (ANCHO_TABLERO * TAMANO_BLOQUE) + MARGEN
SCORE_Y = MARGEN

# Dimensiones de los marcos
GROSOR_MARCO = 2
PADDING_MARCO = 10

# Tamaño de fuentes
FUENTE_TITULO = 24
FUENTE_SCORE = 36

# Colores (RGB)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (40, 40, 40)  # Para el fondo
GRIS_CLARO = (70, 70, 70)  # Para los marcos

# Colores suaves para las piezas
NARANJA_SUAVE = (255, 176, 97)  # Naranja melocotón
AZUL_SUAVE = (135, 206, 235)    # Celeste
VERDE_SUAVE = (152, 251, 152)   # Verde menta
ROJO_SUAVE = (255, 182, 193)    # Rosa claro
MORADO_SUAVE = (221, 160, 221)  # Orquídea
AMARILLO_SUAVE = (255, 229, 124) # Amarillo pastel
CYAN_SUAVE = (175, 238, 238)    # Turquesa claro

# Velocidad del juego
FPS = 10
FPS_DOWN = 30
