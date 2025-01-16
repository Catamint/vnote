import os
import wave
import subprocess
from vosk import Model, KaldiRecognizer
import json

# 定义模型路径
MODEL_PATH = "../models/vosk-model-small-cn-0.22"

# 检查模型是否存在
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Vosk model not found! Download a model from https://alphacephei.com/vosk/models")

# 初始化 Vosk 模型
model = Model(MODEL_PATH)

def convert_audio_to_wav(input_file, output_file):
    """
    将音频转换为 WAV 格式，采样率为 16kHz 单声道。
    """
    command = [
        "ffmpeg",
        "-i", input_file,
        "-ar", "16000",  # 设置采样率为 16kHz
        "-ac", "1",      # 设置为单声道
        "-f", "wav",     # 输出格式为 WAV
        output_file
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return output_file

def transcribe_audio(file_path):
    """
    使用 Vosk 模型将音频转录为文本。
    """
    # 将音频转换为 WAV 格式
    wav_file = os.path.splitext(file_path)[0] + "_converted.wav"
    convert_audio_to_wav(file_path, wav_file)

    # 打开 WAV 文件
    with wave.open(wav_file, "rb") as wf:
        if wf.getnchannels() != 1 or wf.getframerate() != 16000:
            raise ValueError("Audio file must be WAV format with 16kHz sampling rate and mono channel")

        recognizer = KaldiRecognizer(model, wf.getframerate())
        recognizer.SetWords(True)  # 可选：返回词的时间戳
        result = []
        
        # 逐段读取并转录
        while True:
            data = wf.readframes(4000)  # 每次读取 4000 帧
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                partial_result = json.loads(recognizer.Result())['text']
                input(result)
                result.append(partial_result)

        # 获取最终结果
        final_result = recognizer.FinalResult()
        result.append(final_result)

    # 删除临时文件
    os.remove(wav_file)

    # 返回转录结果
    return "\n".join([r for r in result if r.strip()])

if __name__ == "__main__":
    # 测试音频转录
    audio_file = "../data/uploads/mysql.mp4"
    text = transcribe_audio(audio_file)
    with open ("../data/outputs/mysql.txt", "w") as f:
        f.write(text)