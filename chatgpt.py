import openai

# 設置API金鑰
with open('api_key.txt', 'r') as f:
    openai.api_key = f.read()


def chat_with_gpt(topic_content):
    # 初始对话历史
    conversation_history = [
        {"role": "system", "content": topic_content}
    ]

    while True:
        # 用户输入消息
        user_input = input("\nYou: \n")

        if user_input.lower() == "cool":
            print('\nNo sweat! Bye!')
            break

        # 将用户消息添加到对话历史
        conversation_history.append({"role": "user", "content": user_input})

        # 保留最近的 5 则对话
        if len(conversation_history) > 6:  # 初始对话 + 5 则最新对话
            conversation_history = conversation_history[-6:]

        # 发送对话历史并获取助手的回复
        response = openai.chat.completions.create(
            model="gpt-4",  # 使用标准的 GPT-4 模型
            messages=conversation_history,
            temperature=0.7,
        )

        # 提取助手的回复
        assistant_response = response.choices[0].message.content
        token_usage = response.usage.total_tokens
        print('\nChatGPT:', token_usage, '\n', assistant_response)

        # 将助手的回复添加到对话历史
        conversation_history.append({"role": "assistant", "content": assistant_response})

# from my_package.chat import chat_with_gpt

if __name__ == "__main__":
    topic_content = input('How may I help you?\n')
    chat_with_gpt(topic_content)
