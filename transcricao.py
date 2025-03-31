import os
import whisper
import subprocess

def extract_audio(video_path, audio_path):
    """Extrai o áudio do vídeo usando ffmpeg."""
    command = [
        "ffmpeg", "-i", video_path, "-vn", "-acodec", "mp3", audio_path
    ]
    subprocess.run(command, check=True)

def transcribe_audio(audio_path, model_size="small"):
    """Transcreve o áudio usando OpenAI Whisper."""
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result["text"]

def video_to_text(video_path, output_text_path):
    """Converte vídeo em texto e salva a transcrição em um arquivo."""
    audio_path = "temp_audio.mp3"
    
    try:
        # Extraímos o áudio do vídeo
        extract_audio(video_path, audio_path)
        print(f"Áudio extraído com sucesso para {audio_path}")

        # Transcrevemos o áudio extraído
        transcription = transcribe_audio(audio_path)
        print("Transcrição concluída!")

        # Salvamos a transcrição no arquivo
        with open(output_text_path, "w", encoding="utf-8") as f:
            f.write(transcription)

        # Removemos o áudio temporário
        os.remove(audio_path)
        print(f"Transcrição salva em: {output_text_path}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
video_to_text("tema2.mp4", "tema2.txt")
