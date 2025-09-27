# 🤖 Gemini Chatbot with LangGraph + FastAPI + Streamlit

This project is a custom AI chatbot powered by **Google Gemini Pro**, using **LangGraph** for conversation state management. It features a **FastAPI backend** and a **Streamlit frontend** for an interactive UI experience.

---

## 🔧 Tech Stack

| Layer        | Tech Used                     |
|--------------|-------------------------------|
| 💬 Language Model | Google Gemini Pro (`google-generativeai`) |
| 🧠 State Management | LangGraph |
| 🖥️ Backend      | FastAPI + Uvicorn |
| 🌐 Frontend     | Streamlit |
| 📦 Packaging    | pip + virtualenv |

---

## 🚀 Features

- Uses Gemini Pro model via Google GenerativeAI  
- Built on FastAPI + Uvicorn backend  
- Streamlit chat UI  
- LangGraph for conversational memory  
- Mental wellness prompt feature  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YeshwanthrajG/AI-Chatbot-with-FastAPI-and-Streamlit-AgenticAI-VAC.git
```
### 2. Create & Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the backend server

```bash
#Run backend.py
python backend.py
#Server will run on http://127.0.0.1:8000
```

### 5. Start the Frontend App

```bash
#Run frontend.py
streamlit frontend.py
# UI will open at http://localhost:8501
```

---

## 🧪 Sample Questions

```bash
Who is the PM of India?
```

```bash
What is Batman's Origin Story?
```

```bash
Who is Marvel's most powerful character?
```

```bash
Tell me a good joke !!
```

---

## 📄 License
This project is licensed under MIT License. See `LICENSE` file for more details.