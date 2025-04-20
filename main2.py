# for run the program
# After setup location, type these on terminal
# Step 01: .\chatbot\Scripts\activate
# Step 02: python main2.py
# Gemini is used


from openai import OpenAI # type: ignore

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

while True:
    user_input = input("Enter your prompt here: ")

    if user_input =="done":
        break

    completion = client.chat.completions.create(
 
  model="dgoogle/gemini-2.5-pro-exp-03-25:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
    print(completion.choices[0].message.content)