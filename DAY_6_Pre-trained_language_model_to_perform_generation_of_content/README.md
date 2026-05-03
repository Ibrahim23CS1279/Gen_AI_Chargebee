# 🤖 Day 6: Pre-trained Language Model to Perform Generation of Content

This session focuses on building AI chatbots using:

1. Google Generative AI (Gemini)
2. OpenAI API

The chatbot accepts user input and generates AI-based responses using pre-trained language models.

---

# 📌 Topics Covered

* Generative AI basics
* Pre-trained language models
* API integration using Python
* Building terminal-based chatbots
* AI-generated conversations

---

# 📦 Installation

Install required libraries using CMD / Terminal.

## Install Google Generative AI

```bash
pip install -U google-generativeai
```

---

## Install OpenAI

```bash
pip install openai
```

---

# ✅ Verify Installation

Check whether the packages are installed correctly.

## Check Google Generative AI

```bash
pip show google-generativeai
```

---

## Check OpenAI

```bash
pip show openai
```

---

# 💻 Project Files

```text
DAY_6_Pre-trained_language_model_to_perform_generation_of_content/
│
├── README.md
├── chatbot_genai.py
└── chatbot_openai.py
```

---

# 1️⃣ Google Generative AI Chatbot

## 📄 File: chatbot_genai.py

```python
import google.generativeai as genai
import os

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")

chat = model.start_chat(history=[])

print("Ideaslabs Chatbot (Type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        break

    response = chat.send_message(user_input)

    print(f"Ideaslabs: {response.text}")
```

---

# ▶️ Run the Gemini Chatbot

```bash
python chatbot_genai.py
```

---

# 🧠 Sample Conversation

```text
Ideaslabs Chatbot (Type 'exit' to quit)

You: What is Artificial Intelligence?
Ideaslabs: Artificial Intelligence is the simulation of human intelligence by machines.
```

---

# 2️⃣ OpenAI Chatbot

## 📄 File: chatbot_openai.py

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def start_chatbot():
    print("Ideaslabs chatbot, Type 'quit' to exit")

    while True:
        user_input = input("you: ")

        if user_input.lower() in ["quit", "exit"]:
            break

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_input
        )

        reply = response.output[0].content[0].text

        print("Ideaslabs:", reply)

if __name__ == "__main__":
    start_chatbot()
```

---

# ▶️ Run the OpenAI Chatbot

```bash
python chatbot_openai.py
```

---

# ⚠️ Common OpenAI Error

```text
openai.RateLimitError: insufficient_quota
```

## Reason

* API quota exceeded
* Billing not enabled
* Free credits expired

## Solution

* Enable billing in OpenAI dashboard
* Generate a new API key
* Or use Google Generative AI / Hugging Face models

---

# 🔒 Important Security Note

❌ Never upload real API keys to:

* GitHub
* README files
* Screenshots
* Public repositories

Replace real keys with:

```python
YOUR_API_KEY
```

---

# 🎯 Learning Outcomes

By the end of this session, you will understand:

* How Generative AI chatbots work
* Using APIs in Python
* Creating conversational AI systems
* Difference between Gemini and OpenAI APIs
* Handling AI-generated responses

---

# 🚀 Technologies Used

* Python
* Google Generative AI
* OpenAI SDK
* Terminal / CMD

---

# 📚 Future Improvements

* Add Gradio UI
* Voice-enabled chatbot
* Memory-based conversations
* Web deployment
* Hugging Face integration

---

# ✅ Conclusion

This project demonstrates how to integrate pre-trained AI language models into Python applications and create interactive chatbot systems using modern Generative AI APIs.
