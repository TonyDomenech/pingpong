# Ping Pong

Este proyecto incluye un peque\u00f1o juego de ping pong implementado con `pygame`.

## Uso

1. Aseg\u00farate de tener `pygame` instalado. Puedes instalarlo con:

```bash
pip install pygame
```

2. Ejecuta el juego directamente:

```bash
python3 server.py
```

Al iniciarse, ver\u00e1s un men\u00fa con tres modos de juego:

1. **Jugador vs Jugador**
2. **Jugador vs IA**
3. **IA vs IA**

Elige una opci\u00f3n pulsando la tecla correspondiente.

Durante la partida, los controles son:
- Jugador izquierdo: `W` y `S`
- Jugador derecho: flechas arriba y abajo

La IA es intencionalmente irregular: puede cometer errores si la pelota se aleja demasiado, por lo que no siempre alcanzará la pelota.

