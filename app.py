# app/app.py
from flask import Flask, request, render_template, jsonify
from audio_processing.whisper_asr import transcribe_audio
from text_analysis.deepseek_client import analyze_text
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "../data/uploads/"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 保存上传的文件
        audio_file = request.files["audio"]
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_file.filename)
        audio_file.save(file_path)

        # 音频转文本
        text = transcribe_audio(file_path)

        # 文本分析
        api_key = os.getenv("DEEPSEEK_API_KEY")
        summary = analyze_text(text, api_key)

        return jsonify({"transcription": text, "summary": summary})

    return render_template("index.html")  # 上传页面

if __name__ == "__main__":
    app.run(debug=True)
