import openai

openai.api_key = "YOUR_API_KEY"

ret = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "請扮演一位家教老師。用繁體中文回答以下來自學生的問題。"},
        {"role": "user", "content": "大地震發生時，張先生奪門而出，並有心跳加速，血壓上升的現象；這種反應最可能是由下列何種激素引起？(A)胰島素(B)腎上腺素(C)生長激素(D)副甲狀腺。 以上題目為什麼正確答案是B？"}
    ]
)

print(ret.choices[0].message.content)