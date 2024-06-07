import openai

# 設置API金鑰
with open('api_key.txt', 'r') as f:
    openai.api_key = f.read()

# 打開音頻文件

audio_file_path = input('Path of audio file:\n')
with open(audio_file_path, 'rb') as audio_file:
    # 轉譯成文字 模型是whisper
    response = openai.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
transcript = response.text

# 將轉譯結果寫入文件
transcript_path = 'transcript.txt'
with open(transcript_path, 'w') as f:
    f.write(transcript)

# 檔案儲存完畢
print(f"Transcript saved to {transcript_path}")
