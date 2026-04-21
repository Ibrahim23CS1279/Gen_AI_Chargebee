# 🤖 Day 5: Python for Generative AI (Hugging Face + Colab)

This session focuses on running Generative AI models using Python in Google Colab and exploring real-world AI tools.

---

## 📌 Topics Covered

### 1. Running Python in Google Colab

* Cloud-based Python environment
* No local setup required
* Easy GPU/CPU access

---

### 2. Hugging Face Models

Using pre-trained models from Hugging Face to perform:

* Text generation
* Summarization
* Question answering

---

### 3. Example Workflow

* Load model from Hugging Face
* Run inference in Colab
* Generate output

---

## 🔗 Colab Notebook

👉 View the notebook here:
[Open Colab Notebook](https://colab.research.google.com/drive/1ZF4zG9VFdCtPk-YY9uUrdEsamRwilzLC?usp=sharing)

---

## 💡 Sample Code (Hugging Face Transformers)

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("AI is transforming the world because", max_length=30)
print(result)
```

---

## 🌐 AI Tools Explored

### 🧠 Cursor AI

Cursor AI
AI-powered code editor that helps write and debug code faster.

---

### 🔍 Toolify AI

Toolify AI
Platform to discover various AI tools across categories.

---

### 🎨 Dora AI

Dora AI
AI-based website design and generation tool.

---

### 🔊 ElevenLabs

ElevenLabs
Used for realistic text-to-speech generation.

---

### 📞 Callin.io

Callin.io
AI voice agents for calls and automation.

---

## 🎯 Learning Outcomes

By the end of this session, you should:

* Understand how to run GenAI models in Colab
* Use Hugging Face pipelines
* Explore real-world AI tools
* Know how to integrate AI into applications

---

## ⚠️ Notes

* Internet connection required for Colab
* Models may take time to load
* Some models require GPU for better performance

---

## 🚀 Next Step

Day 6: Advanced Model Usage & Integration
