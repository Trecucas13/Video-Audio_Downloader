# Video-Audio_Downloader

Aplicativo para descargar videos de YouTube y recortarlos a un segmento específico.

## Features

- Descarga videos directamente desde URLs de YouTube.
- Permite especificar un minuto de inicio y un minuto de fin para recortar el video.
- Guarda el video recortado como `video_recortado.mp4`.
- Limpia automáticamente el archivo de video original descargado.

## Requirements

Para ejecutar este script, necesitarás tener instaladas las siguientes bibliotecas de Python:

- pytube
- moviepy

Puedes instalarlas usando pip:
```bash
pip install pytube moviepy
```

## Usage

1.  Clona este repositorio o descarga el archivo `descar.py`.
2.  Asegúrate de tener Python instalado en tu sistema.
3.  Instala las bibliotecas requeridas (ver la sección de Requisitos).
4.  Ejecuta el script desde tu terminal:
    ```bash
    python descar.py
    ```
5.  El script te pedirá:
    - La URL del video de YouTube que deseas descargar.
    - El minuto de INICIO desde el cual quieres recortar el video (por ejemplo, `0`).
    - El minuto FINAL hasta el cual quieres recortar el video (por ejemplo, `1`).

### Example

```bash
python descar.py
```

Luego, cuando se te solicite:

```
👇 Pega esta URL para probar (funciona):
https://www.youtube.com/watch?v=dQw4w9WgXcQ

🎯 URL del video: https://www.youtube.com/watch?v=dQw4w9WgXcQ
⏱ Minuto de INICIO (ej: 0): 1
⏱ Minuto FINAL (ej: 1): 2
```

Esto descargará el video, lo recortará desde el minuto 1 hasta el minuto 2, y guardará el resultado como `video_recortado.mp4`.

## License

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
