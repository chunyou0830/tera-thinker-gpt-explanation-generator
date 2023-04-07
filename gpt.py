import openai

question = input("輸入題目敘述：")
choices = input("輸入題目選項：")
correct_answer = input("輸入正確選項代碼：")

openai.api_key = "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"

ret = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "請扮演一位家教老師。以繁體中文回答以下來自學生的問題，並只以題目敘述和高中生的知識針對題目各個選項進行解釋。"},
        {"role": "user", "content": """{}{}以上題目為什麼正確答案是{}？""".format(question,choices,correct_answer)},
    ]
)

print("\n")
print(ret.choices[0].message.content)