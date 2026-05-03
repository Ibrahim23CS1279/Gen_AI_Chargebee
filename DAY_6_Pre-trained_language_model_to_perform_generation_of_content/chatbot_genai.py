import google.generativeai as genai
import os

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model=genai.GenerativeModel("gemini-3.1-flash-lite-preview");
chat=model.start_chat(history=[])

print("Ideaslabs Chatbot {Type 'exit' to quit)")

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit","quit","bye"]:
        break
    response=chat.send_message(user_input)
    print(f"Ideaslabs:{response.text}")


