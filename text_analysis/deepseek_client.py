# text_analysis/deepseek_client.py
import sys
import os

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import config
from openai import OpenAI
import json

# 设置 OpenAI API 密钥
client = OpenAI(api_key=config.DEEPSEEK_API_KEY , base_url="https://api.deepseek.com")

def summarize_text(input_text, model="gpt-4", max_tokens=300):
    """
    使用 OpenAI API 对文本进行分析和总结。

    Args:
        input_text (str): 要总结的文本。
        model (str): 使用的 OpenAI 模型，默认为 gpt-4。
        max_tokens (int): 输出总结的最大 token 数。

    Returns:
        str: 总结后的文本。
    """
    try:
        # 调用 OpenAI API 完成文本总结
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an expert summarizer."},
                {"role": "user", "content": f"This is a speech-to-text result, try to restore the text: {input_text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.5,  # 控制总结的随机性
            stream=False,
        )
        # 提取总结文本
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return None


if __name__ == "__main__":
    with open("../data/outputs/mysql.txt", "r") as f:
        text = f.read()
    result = summarize_text(text)
    print(result)