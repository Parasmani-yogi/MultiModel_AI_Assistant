# 🤖 Multimodal AI Assistant

A ChatGPT-like **Multimodal AI Assistant** built using **Streamlit + OpenAI APIs**, supporting text, image, and voice-based interactions with a clean multi-chat interface.

---

## 🚀 Features


### 💬 Chat System
- Multiple independent chat sessions
- Sidebar chat history (like ChatGPT)
- Rename chat functionality
- No cross-chat mixing (each chat has isolated memory)

### 🧠 AI Capabilities
- Context-aware conversation
- Supports text + image queries
- Maintains short-term conversation history

### 🖼️ Image Input
- Upload images directly
- Ask questions related to the image
- AI responds using multimodal understanding

### 🎤 Voice Input
- Record voice using microphone
- Automatic speech-to-text conversion (Whisper)
- Auto-send query after recording stops
- No manual send required

### 🎨 UI/UX
- Clean ChatGPT-inspired interface
- Input bar appears below last message
- Inline “+” action panel for multimodal inputs
- Smooth chat experience

---

## 🏗️ Project Structure

multimodal-ai-assistant/
│
├── app.py                  # Main Streamlit application
│
├── core/
│   ├── llm.py              # OpenAI API interaction
│   ├── speech.py           # Voice transcription (Whisper)
│   ├── vision.py           # Image handling (extendable)
│   ├── memory.py           # Chat memory management
│
├── utils/
│   ├── helpers.py          # File handling utilities
│   ├── prompts.py          # Prompt templates (optional)
│
├── assets/
│   └── temp/               # Temporary storage (images/audio)
│
├── requirements.txt
├── .env
└── README.md

---

## ⚙️ Installation

### 1. Clone Repository
git clone https://github.com/your-username/multimodal-ai-assistant.git
cd multimodal-ai-assistant

### 2. Create Virtual Environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

OPENAI_API_KEY=your_api_key_here

---

## ▶️ Run the Application

streamlit run app.py

Open in browser:
http://localhost:8501

---

## 🧠 How It Works

### Chat Handling
- Each chat is stored separately in session state
- Messages are appended per chat
- No overlap between chats

### Multimodal Processing
- Text → sent directly to LLM
- Image → encoded and sent with query
- Voice → transcribed using Whisper → sent as text

### Context Awareness
- Recent messages are passed to the model
- Enables conversational continuity

---

## 🛠️ Tech Stack

- Frontend: Streamlit
- Backend: Python
- LLM: OpenAI (gpt-4o-mini)
- Speech-to-Text: Whisper API

---

## 📌 Key Highlights

- Modular and scalable architecture
- Real-world chat system implementation
- Multimodal AI integration
- Clean and user-friendly UI

---

## ⚠️ Limitations

- Voice input requires browser microphone permission
- Streamlit has limited frontend flexibility
- Chats are not persisted (session-based)

---

## 🚀 Future Improvements

- Persistent chat storage (SQLite / MongoDB)
- Streaming responses (typing animation)
- Drag-and-drop image upload
- Inline mic & image icons (ChatGPT-style)
- LangChain / AI agent integration
- Cloud deployment

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests.
Suggestions and improvements are always welcome.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Parasmani Yogi

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!