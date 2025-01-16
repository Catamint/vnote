# text_analysis/deepseek_client.py
import requests

def analyze_text(text, api_key):
    url = "https://api.deepseek.com/analyze"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"text": text, "language": "en"}  # 支持的语言可以配置
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()  # 返回分析结果
    else:
        raise Exception(f"DeepSeek API Error: {response.text}")
