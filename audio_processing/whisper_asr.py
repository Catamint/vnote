# audio_processing/whisper_asr.py
import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # 或选择 "small", "large"
    result = model.transcribe(file_path)
    return result["text"]
