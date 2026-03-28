# 🤖 Multimodal AI Assistant

A modern AI assistant built using Streamlit and OpenAI APIs, supporting text, image, and voice interactions with a clean multi-chat interface.

---

## 🚀 Features

- 💬 Multiple chat sessions (ChatGPT-style)
- 🧠 Context-aware AI responses
- 🖼️ Image upload + question answering
- 🎤 Voice input with automatic transcription
- ✏️ Rename chat functionality
- 🔒 Isolated chat memory (no mixing between chats)
- ⚡ Simple and clean user interface

---

## ⚙️ Setup (Using uv)

### 1. Install uv

```bash
pip install uv
```

### 2. Create Virtual Environment
```bash
uv venv
```

### 3. Activate Environment

Windows:
```bash
.venv\Scripts\activate
```

Mac/Linux:
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

`
OPENAI_API_KEY=your_api_key_here
`

---

## ▶️ Run the Application
```bash
streamlit run app.py
```


---

## 🧠 How It Works

- Each chat session is stored independently
- Only selected chat history is used for responses
- Supports text, image, and voice inputs
- Voice input is converted to text before processing
- Context from recent messages improves responses

---

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenAI API (GPT + Whisper)
- uv (environment and dependency management)

---

## ⚠️ Notes

- Voice input requires browser microphone permission
- Works best on Chrome browser
- Chats are session-based (not permanently stored)

---

## 🚀 Future Improvements

- Persistent chat storage (database)
- Streaming responses
- Drag-and-drop image upload




