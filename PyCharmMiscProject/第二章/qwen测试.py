import ollama

def chat_stream():
    print("AI：", end="")

    stream = ollama.chat(
        model="qwen3:14b",
        messages=[
            # 第1条：设定AI的身份（名字、性格）
            {"role": "system", "content": "你是一个AI助理，你的名字叫花朵"},
            # 第2条：你真正的问题
            {"role": "user", "content": "你觉得这个名字怎么样？"}
        ],
        stream=True
    )

    for chunk in stream:
        content = chunk["message"]["content"]
        if content:
            print(content, end="", flush=True)
    print()

if __name__ == "__main__":
    chat_stream()

