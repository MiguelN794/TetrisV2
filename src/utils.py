def rotar_matriz(matriz):
    """Rota una matriz 90 grados en sentido horario."""
    return [list(reversed(col)) for col in zip(*matriz)]
