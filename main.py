# for run the program
# After setup location, type these on terminal
# Step 01: .\chatbot\Scripts\activate
# Step 02: python main.py
# Deepseek is used


from openai import OpenAI # type: ignore

import os  # in the computer system

api_key = os.getenv("ChatBotKey")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key = api_key,
)

chat_history =[]     # variable

personas = {
   "default": "You are a helpful AI Assistant",
   "sarcastic": "You are a sarcastic AI who gives witty and mocking responses",
   "poet": "You are a poetic AI that responds in rhymes and verses"
}

print("Choose a persona : (default/ sarcastic / poet)")

user_persona_input = input("Enter persona :").strip().lower()

# personas= personas.get(user_persona_input) 

chat_history.append({
   "role": "system",
   "content": personas[user_persona_input]
 })

while True:
    user_input = input("Enter your prompt here: ")

    if user_input == 'clear':
       chat_history = []
       chat_history.append({"role": "system", "content": personas[user_persona_input]})

       print("Chat history cleared")
       continue
    

    chat_history.append({ 
      "role": "user",
      "content": user_input
    })
 
    if user_input =="exit":
      break
  

    completion = client.chat.completions.create(
 
    model="deepseek/deepseek-r1-zero:free",
    messages=chat_history
    )
    response = completion.choices[0].message.content   
    print(response)

    chat_history.append({
       "role" : "user",
       "content" : response
    })