# Tetris en Python

Este es un proyecto de Tetris implementado en Python utilizando la biblioteca Pygame. El objetivo del juego es encajar las piezas que caen para formar líneas completas y eliminarlas, acumulando puntos en el proceso.

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/tu-usuario/tetris-python.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd tetris-python
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install pygame
    ```

## Uso

Para ejecutar el juego, simplemente ejecuta el archivo `game.py`:

```bash
python src/game.py
```

## Controles

- **Flecha Izquierda**: Mover la pieza a la izquierda.
- **Flecha Derecha**: Mover la pieza a la derecha.
- **Flecha Abajo**: Acelerar la caída de la pieza.
- **Barra Espaciadora**: Mover la pieza al fondo instantáneamente.
- **Shift Izquierdo**: Almacenar o cambiar la pieza actual.

## Estructura del Proyecto

```
src/
  game.py        # Archivo principal del juego.
  tablero.py     # Lógica del tablero de juego.
  pieza.py       # Definición de las piezas del Tetris.
  constantes.py  # Definición de constantes utilizadas en el juego.
  utils.py       # Funciones utilitarias.
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama:
    ```bash
    git checkout -b feature/nueva-funcionalidad
    ```
3. Realiza tus cambios y haz commit:
    ```bash
    git commit -am 'Añadir nueva funcionalidad'
    ```
4. Haz push a la rama:
    ```bash
    git push origin feature/nueva-funcionalidad
    ```
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Créditos

Este proyecto fue desarrollado por [Tu Nombre]. Si tienes alguna pregunta o sugerencia, no dudes en contactarme.

