
# 🧠 LangChain + Groq AI Chatbot with Memory & Structured Output

This project demonstrates a powerful integration of **LangChain** with **Groq's LLaMA 3.1 8B Instant** model to create:

- A **multi-session chatbot** with memory.
- A **structured data extractor** using Pydantic.
- A **rate-limited memory chain** to simulate memory window constraints.

---

## 🚀 Features

- ✅ Multi-session memory using `RunnableWithMessageHistory`
- ✅ File-based memory using `FileChatMessageHistory`
- ✅ Rate-limited memory via custom slicing function
- ✅ Structured classification with Pydantic schema (sentiment, political leaning, language)
- ✅ Easy session switching and tracking using dictionary keys

---

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/)
- [Groq](https://console.groq.com/)
- [Python](https://www.python.org/)
- [Pydantic](https://docs.pydantic.dev/)
- `dotenv` for environment variables

---

## 📁 Project Structure

.
├── .env # Contains GROQ_API_KEY
├── memory_chatbot.py # Chatbot with memory sessions
├── structured_extractor.py # Text-to-structure classification logic
├── messages.json # File-based memory history (auto-generated)
└── requirements.txt



---

## ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/langchain-groq-chatbot.git
   cd langchain-groq-chatbot
    Install dependencies

    pip install -r requirements.txt
    Add your Groq API Key
    
    Create a .env file and add:
    
    GROQ_API_KEY=your_groq_api_key_here
    🧪 How to Run
    🧠 Memory Chatbot
    python memory_chatbot.py
Features:

Remembers facts like names and favorite colors across sessions.

Supports limited memory mode to simulate rate limiting.

## 📊 Structured Extraction

python structured_extractor.py
Input: Long or short-form text.
Output: Sentiment, political leaning, and language in structured format.

## 💬 Example: Memory Sessions
pgsql

Session 1:
User: My name is Mihir
User: What is my name?
Bot: Your name is Mihir.

Session 2:
User: My name is Raj
User: What is my name?
Bot: Your name is Raj.

## 📊 Example: Structured Classification
Input: "I believe President Biden's approach is necessary and progressive."
Output:
{
  "sentiment": "soft",
  "political_tendency": "With Biden",
  "language": "English"
}
## 📌 TODO
 Add streaming support

 Add FastAPI/Streamlit web interface

 Dockerize the project

 Add test cases

## 📄 License
MIT License. See the LICENSE file for details.

## 🙌 Acknowledgements

LangChain

Groq

Pydantic



