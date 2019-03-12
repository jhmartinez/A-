# AStar
Algoritmo A*
Requerimientos:
Python == 3.7.x
pygame == 1.9.4

Puede instalar Python desde la siguiente dirección:
- https://www.python.org/

Para instalar pygame puede utilizar el sistema de gestión de paquetes: (pip), el cual debe venir incluido por defecto
con Python. Desde el directorio raíz de la aplicación puede ejecutar el siguiente comando para instalar pygame
pip install -r requirements.txt, o puede instalarlo de la siguiente forma: pip install pygame==1.9.4

Formas de ejecución de la aplicación:
python main.py -mode:console
python main.py -mode:window
Nota: Invocar a main.py desde el directorio raiz de la aplicación: (..\AAster\)

Controles de la aplicación en modo ventana:
- Barra de Espacio: Ejecutar el algoritmo y el jugador puede moverse entre las casillas hasta llegar a la meta a partir del camino
encontrado.
- Con los controles K_ABAJO o K_DERECHA puede moverse hacia la próxima casilla.
- Con los controles K_ARRIBA o K_IZQUIERDA puede moverse hacia la casilla anterior.
