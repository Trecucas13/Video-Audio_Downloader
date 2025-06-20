from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def descargar_video(url, inicio, fin):
    try:
        yt = YouTube(url)
        print(f"🎬 Título del video: {yt.title}")

        # Seleccionar stream MP4 con video y audio
        stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
        if not stream:
            print("❌ No se encontró un stream compatible en mp4.")
            return

        # Descargar
        print("⬇️ Descargando video completo...")
        stream.download(filename="video_original.mp4")
        print("✅ Descarga completa.")

        # Recortar con MoviePy
        print(f"✂️ Recortando desde {inicio} hasta {fin} minutos...")
        clip = VideoFileClip("video_original.mp4").subclip(inicio * 60, fin * 60)
        clip.write_videofile("video_recortado.mp4")
        print("✅ Video recortado guardado como 'video_recortado.mp4'")

        # Limpiar
        os.remove("video_original.mp4")

    except Exception as e:
        print("⚠️ Error:", e)

# ==== USO ====
if __name__ == "__main__":
    print("👇 Pega esta URL para probar (funciona):")
    print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    url = input("\n🎯 URL del video: ").strip()
    inicio = int(input("⏱ Minuto de INICIO (ej: 0): "))
    fin = int(input("⏱ Minuto FINAL (ej: 1): "))

    descargar_video(url, inicio, fin)
