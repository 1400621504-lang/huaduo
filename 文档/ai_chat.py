import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "请分析用户输入的情感，只返回 JSON 格式，不要其他文字：{\"sentiment\": \"正面/负面/中性\", \"score\": 0-10}"},
        {"role": "user", "content": "今天天气真好，出去玩了一趟，很开心！"}
    ]
)

reply = response.choices[0].message.content
print("AI 原始回复:", reply)

# 解析 JSON
try:
    data = json.loads(reply)
    print(f"情感: {data['sentiment']}")
    print(f"分数: {data['score']}")
except:
    print("JSON 解析失败")

# ===== Temperature 对比实验 =====
prompt = "用一句话描述春天"

for temp in [0, 0.7, 1.2,2]:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp
    )
    print(f"\n--- temperature={temp} ---")
    print(response.choices[0].message.content)
