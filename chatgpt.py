import openai

with open('api_key.txt', 'r') as f:
    openai.api_key = f.read()

topic_content = input('How may I help you?\n')

# 初始對話歷史
conversation_history = [
    {"role": "system", "content": topic_content}
]

while True:
    # 使用者輸入消息
    user_input = input("\nYou: \n")

    if user_input.lower() == "cool":
        print('\nNo sweat! Bye!')
        break

    # 將使用者消息添加到對話歷史
    conversation_history.append({"role": "user", "content": user_input})

    # 保留最近的5則對話
    if len(conversation_history) > 6:  # 初始對話 + 5則最新對話
        conversation_history = conversation_history[-6:]

    # 發送對話歷史並獲取助手的回覆
    response = openai.chat.completions.create(
        model="gpt-4",  # 使用標準的 GPT-4 模型
        messages=conversation_history,
        temperature=0.7,
    )

    # 提取助手的回覆
    assistant_response = response.choices[0].message.content
    token_usage = response.usage.total_tokens
    print('\nChatGPT:', token_usage, '\n', assistant_response)
    print('\n')

    # 將助手的回覆添加到對話歷史
    conversation_history.append({"role": "assistant", "content": assistant_response})