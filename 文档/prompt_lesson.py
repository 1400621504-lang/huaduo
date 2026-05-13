# from openai import OpenAI

# client = OpenAI(
#     api_key="sk-31936afa61424bd3b646ce8ff333f077",
#     base_url="https://api.deepseek.com"
# )

# # 给 3 个例子，让 AI 学会格式
# messages = [
#     {"role": "system", "content": "将句子翻译为客服回复，格式：\"问题：xxx\n回复：xxx\""},
#     {"role": "user", "content": "我要退货"},
#     {"role": "assistant", "content": "问题：我要退货\n回复：好的，请问您的订单号是多少？"},
#     {"role": "user", "content": "什么时候发货"},
#     {"role": "assistant", "content": "问题：什么时候发货\n回复：您的订单预计 2-3 天内发出，请耐心等待。"},
#     {"role": "user", "content": "能便宜点吗"},
#     {"role": "assistant", "content": "问题：能便宜点吗\n回复：目前商品已是优惠价格，暂不支持议价哦。"},
#     # 现在让 AI 自己回复新的问题
#     {"role": "user", "content": "新年快乐"}
# ]

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=messages,
#     temperature=0.3
# )

# print(response.choices[0].message.content)


# # def analyze_review(text, target_language="中文"):
# #     prompt = f"""
# # 分析以下产品评价：
# # 1. 情感（正面/负面/中性）
# # 2. 评分（0-100）
# # 3. 用{target_language}总结关键问题

# # 评价：{text}
# # """
# #     response = client.chat.completions.create(
# #         model="deepseek-chat",
# #         messages=[{"role": "user", "content": prompt}],
# #         temperature=1
# #     )
# #     return response.choices[0].message.content

# # # 测试几个评论
# # reviews = [
# #     "手机用了两天就死机了，垃圾产品",
# #     "性价比很高，推荐购买",
# #     "一般般吧，没有想象中好"
# # ]

# # for r in reviews:
# #     print("---")
# #     print(analyze_review(r))
# # 不加思维链
# # response = client.chat.completions.create(
# #     model="deepseek-chat",
# #     messages=[{"role": "user", "content": "小明有 5 个苹果，给了小红 2 个，又买了 3 个，现在有几个？"}],
# #     temperature=0
# # )
# # print("直接回答:", response.choices[0].message.content)

# # # 加思维链
# # response = client.chat.completions.create(
# #     model="deepseek-chat",
# #     messages=[{"role": "user", "content": "小明有 5 个苹果，给了小红 2 个，又买了 3 个，现在有几个？\n请一步步思考。"}],
# #     temperature=0
# # )
# # print("\n思维链回答:", response.choices[0].message.content)
# # 角色 A：严肃专家
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "你是一个资深 Python 技术专家，回答简短专业，直接给代码。"},
#         {"role": "user", "content": "怎么读取 CSV 文件"}
#     ],
#     temperature=0
# )
# print("专家模式:", response.choices[0].message.content)

# # 角色 B：老师
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "你是一个耐心的编程老师，用通俗易懂的方式讲解，适合初学者。"},
#         {"role": "user", "content": "怎么读取 CSV 文件"}
#     ],
#     temperature=0
# )
# print("\n老师模式:", response.choices[0].message.content)


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 几条新闻标题（你可以自己改）
news_list = [
    "OpenAI 发布 GPT-5，性能提升 10 倍",
    "苹果公司市值突破 4 万亿美元",
    "国内新能源汽车销量再创新高",
    "研究发现每天运动 30 分钟可延长寿命 5 年",
    "淘宝全面接入 AI 客服"
]

news_text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(news_list)])

prompt = f"""
你是 AI 日报编辑，根据以下新闻生成日报。

要求：
- 用 Markdown 格式
- 每条新闻包含：摘要（20字内）、分类（科技/财经/社会等）、关键词
- 最后加一句今日点评

新闻：
{news_text}
"""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3,
    stream= True
)

print("=" * 30 + " AI 日报 " + "=" * 30)
for chunk in response:
    content = chunk.choices[0].delta.content or ""
    print(content, end="", flush=True)
print()
print("=" * 70)
