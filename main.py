from moviepy import VideoFileClip, concatenate_videoclips
from pathlib import Path

# Ruta al directorio actual donde está la carpeta con los videos
carpeta_videos = "Videos"  # Reemplaza esto con el nombre de tu carpeta
directorio = Path(__file__).parent / carpeta_videos

# Ordenar los videos por nombre (alfabéticamente)
videos = sorted(directorio.glob("*.mp4"))

# Cargar los videos en MoviePy
clips = [VideoFileClip(str(video)) for video in videos]

# Unir los clips
video_final = concatenate_videoclips(clips)

# Guardar el video unido en la misma carpeta
video_final.write_videofile(str(Path(__file__).parent/ "VideoResult" / "video_unido.mp4"), codec="libx264", audio_codec="aac")
