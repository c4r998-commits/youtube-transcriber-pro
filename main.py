from youtube_transcript_api import YouTubeTranscriptApi
import sys

def obtener_transcripcion(video_id):
    try:
        # Obtenemos la transcripción en español por defecto, o en inglés si no está disponible
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en'])
        
        texto_completo = ""
        for item in transcript_list:
            texto_completo += f"[{item['start']:.2f}s] {item['text']}\n"
            
        return texto_completo
    except Exception as e:
        return f"Error al obtener la transcripción: {str(e)}"

if __name__ == "__main__":
    print("--- Transcriptor de YouTube Activo ---")
    # Ejemplo de uso con un ID de video de YouTube (puedes cambiarlo después)
    # El ID es lo que va después de 'watch?v=' en el enlace de YouTube
    video_id_ejemplo = "dQw4w9WgXcQ" 
    
    print(f"Obteniendo transcripción para el video ID: {video_id_ejemplo}...")
    resultado = obtener_transcripcion(video_id_ejemplo)
    print("\nResultado:")
    print(resultado)
