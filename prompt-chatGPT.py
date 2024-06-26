!pip install openai

import openai
openai.api_key = ""

model_engine = "text-davinci-003"
while True:
  prompt = input('Brief: ')
  completion = openai.Completion.create(engine = model_engine, 
                                        prompt = prompt, 
                                        max_tokens = 1500, 
                                        temperature = 0.8)
  message = completion.choices[0].text
  print(message)
