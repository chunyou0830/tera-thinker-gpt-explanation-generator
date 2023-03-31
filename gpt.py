import openai

openai.api_key = "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"

ret = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "請扮演一位家教老師。以繁體中文回答以下來自學生的問題，並只以題目敘述和高中生的知識針對題目各個選項進行解釋。"},
        {"role": "user", "content": """大文看見桌上有四種生物的學名分別為：Dryas octopetala，Arnica cordifolia，Dryas bipetala和Kandelia octopetala。哪兩種生物的親緣關係最相近？
        (A)Dryas octopetala和Dryas bipetala
        (B)Dryas octopetala和Kandelia octopetala
        (C)Kandelia octopetala和Arnica cordifolia
        (D)Arnica cordifolia和Dryas bipetala。
        以上題目為什麼正確答案是A？"""},

    ]
)

print(ret.choices[0].message.content)