from flask import Flask, request, jsonify
from flask_cors import CORS
from audio_processing.vosk_asr import transcribe_audio
from text_analysis.deepseek_client import summarize_text
import os

app = Flask(__name__)
CORS(app)  # 允许跨域请求

UPLOAD_FOLDER = './data/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_and_process():
    """
    接收音频文件，进行转录和文本总结处理。
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio_file = request.files['file']
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 保存音频文件
    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    try:
        # Step 1: 音频转文本
        transcription_results = transcribe_audio(file_path)
        full_text = transcription_results
        input(full_text)
        
        # Step 2: 文本总结
        summary = summarize_text(full_text)

        # 返回结果
        return jsonify({
            "original_text": full_text,
            "summary": summary
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # 清理上传的文件
        # os.remove(file_path)
        pass

@app.route('/')
def health_check():
    """
    健康检查接口。
    """
    return jsonify({"status": "Server is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
