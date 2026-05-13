import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ChatBot:
    def __init__(self, api_key, base_url, model="deepseek-chat", temperature=0.7):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.temperature = temperature
        self.messages = [{"role": "system", "content": "你是一个友好的 AI 助手，回答简洁有用。"}]
    
    def ask(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature,
            stream=True
        )
        reply = ""
        print("AI: ", end="", flush=True)
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            print(content, end="", flush=True)
            reply += content
        print()
        self.messages.append({"role": "assistant", "content": reply})
        return reply
    
    def clear(self):
        self.messages = [self.messages[0]]
    
    def set_model(self, model):
        self.model = model
    
    def set_temperature(self, temp):
        self.temperature = temp


# 使用
bot = ChatBot(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

while True:
    user_input = input("\n你: ")
    if user_input == "/exit":
        print("AI: 再见！")
        break
    elif user_input == "/clear":
        bot.clear()
        print("AI: 历史已清空")
        continue
    elif user_input.startswith("/model "):
        bot.set_model(user_input[7:])
        print(f"AI: 已切换模型为 {user_input[7:]}")
        continue
    elif user_input.startswith("/temp "):
        bot.set_temperature(float(user_input[6:]))
        print(f"AI: 已设置 temperature 为 {user_input[6:]}")
        continue
    
    bot.ask(user_input)
