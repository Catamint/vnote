以下是项目的 README 文件，适用于最终采用 DeepSeek 进行文本分析与总结的版本。

---

# **Audio Summarizer**

## **项目简介**
Audio Summarizer 是一个简单的音频处理应用，支持从音频文件中提取文本并生成总结笔记。  
项目采用以下技术栈：
- **音频转文本**：基于 Vosk 轻量级离线 ASR（自动语音识别）模型。
- **文本分析与总结**：通过 [DeepSeek API](https://deepseek.tech) 提供高效的文本处理和总结服务。
- **前端界面**：使用 HTML 和 JavaScript 构建静态网页，用于音频上传和结果展示。
- **后端服务**：基于 Flask 框架提供 API 接口，集成 Vosk 和 DeepSeek。

---

## **功能特点**
1. **音频文件上传**：支持 `.wav`, `.mp3` 等常见格式的音频文件。
2. **音频转录**：将音频内容转录为文本。
3. **文本总结**：通过 DeepSeek API 自动生成简洁易读的文本摘要。
4. **静态网页测试**：提供简单易用的前端测试界面。

---

## **安装与运行**

### **环境要求**
- Python 3.8 或更高版本
- 推荐的系统环境：Windows/Linux/macOS

### **依赖安装**
1. 克隆项目代码：
   ```bash
   git clone https://github.com/your-repo/audio-summarizer.git
   cd audio-summarizer
   ```

2. 安装依赖库：
   ```bash
   pip install -r requirements.txt
   ```

3. 下载 Vosk 模型：
   - 访问 [Vosk 官方模型页面](https://alphacephei.com/vosk/models)。
   - 下载适合的语言模型（如 `vosk-model-small-en-us`）。
   - 解压后将模型目录放置在项目根目录下，例如 `./vosk_model`。

4. 配置 DeepSeek API 密钥：
   - 在项目目录中创建 `.env` 文件，添加以下内容：
     ```env
     DEEPSEEK_API_KEY=your-deepseek-api-key
     ```

---

### **运行项目**
1. 启动 Flask 服务：
   ```bash
   python app.py
   ```
   默认服务器地址为 `http://localhost:5000`。

2. 打开静态网页：
   - 使用浏览器直接打开 `static/index.html`。
   - 上传音频文件，查看转录和总结结果。

---

## **项目结构**
```
audio-summarizer/
├── app.py                      # Flask 后端主程序
├── audio_processing/
│   ├── __init__.py
│   └── vosk_asr.py             # 音频转文本模块
├── text_analysis/
│   ├── __init__.py
│   └── deepseek_summary.py     # 文本分析与总结模块
├── static/
│   └── index.html              # 前端静态网页
├── uploads/                    # 上传音频文件的临时存储
├── vosk_model/                 # Vosk 模型目录（需手动下载）
├── requirements.txt            # 项目依赖列表
└── README.md                   # 项目说明文档
```

---

## **API 说明**

### **1. POST /upload**
用于接收音频文件并返回转录和总结结果。

- **请求参数**：
  - `file`：上传的音频文件。

- **响应数据**：
  ```json
  {
    "original_text": "完整的转录文本",
    "summary": "文本总结内容"
  }
  ```

- **错误示例**：
  ```json
  {
    "error": "错误信息"
  }
  ```

---

## **示例代码**
### **音频上传与处理**
以下是一个 Python 客户端示例代码：
```python
import requests

url = "http://localhost:5000/upload"
file_path = "example_audio.wav"

with open(file_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

if response.status_code == 200:
    result = response.json()
    print("Original Text:", result["original_text"])
    print("Summary:", result["summary"])
else:
    print("Error:", response.json().get("error"))
```

---

## **注意事项**
1. **DeepSeek API 限制**：
   - 请确保您的 DeepSeek API 密钥有效。
   - 如果请求频率过高或超出配额，请参考 [DeepSeek 文档](https://deepseek.tech/docs) 调整调用策略。

2. **Vosk 模型兼容性**：
   - 选择适合目标语言的模型（如英语或中文）。
   - 大型模型提供更高准确率，但处理速度较慢。

3. **性能优化**：
   - 长音频文件可以分段处理以减少单次请求的负担。
   - 在生产环境中，可考虑使用更强大的硬件以提升性能。

---

## **许可证**
本项目遵循 MIT 许可证，详情请参阅 [LICENSE](LICENSE)。

---

如需帮助或反馈问题，请随时联系！