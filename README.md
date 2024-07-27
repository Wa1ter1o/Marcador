# Marcador
Marcador de tenis de mesa para dos jugadores

Programa hecho con Python 3.10 y pygame 2.1.2

La versión más optimizada se encuentra en la rama 'raspi', por lo que funciona bien en una raspberry pi 4 o 400

### Actualizar pygame a 2.1.2 en raspberry:
- ingresar a al terminal

    ```shell
    python3 -m pip install pygame==2.1.2
    ```
- instalar dependencias

    ```shell
    sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0 libsdl2-ttf-2.0-0
    ```

### Iniciar el marcador al encender:

- abre la terminal y colocate en /etc/xdg/autostart


Puedes agregar la música de tu preferencia en en las carpeta assets/sonidos/fondo , crea una nueva carpeta para agregar una categoría y dentro de ella ingresa tus pistas
musicales preferidas.  El programa las reconocerá

Que lo disfruten
