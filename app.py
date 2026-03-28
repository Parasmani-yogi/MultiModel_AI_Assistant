import streamlit as st
import os
import hashlib
from core.llm import get_response
from core.speech import transcribe
from core.memory import add_message
from utils.helpers import save_uploaded_file

st.set_page_config(page_title="Multimodal AI Assistant", layout="wide")

# ---------------- INIT ----------------
os.makedirs("assets/temp", exist_ok=True)

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0

if "show_menu" not in st.session_state:
    st.session_state.show_menu = False

if "rename_mode" not in st.session_state:
    st.session_state.rename_mode = False

#  FIX: voice tracking
if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None


# ---------------- FUNCTIONS ----------------
def generate_chat_title(text):
    return text[:30] + "..." if len(text) > 30 else text


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("💬 Chats")

    if st.button("➕ New Chat"):
        st.session_state.chat_count += 1
        chat_id = f"chat_{st.session_state.chat_count}"

        st.session_state.chats[chat_id] = {
            "messages": [],
            "title": "New Chat"
        }

        st.session_state.current_chat = chat_id
        st.session_state.show_menu = False

    st.divider()

    for chat_id, chat_data in st.session_state.chats.items():

        col1, col2 = st.columns([4, 1])

        with col1:
            if st.button(chat_data["title"], key=f"chat_{chat_id}"):
                st.session_state.current_chat = chat_id
                st.session_state.show_menu = False

        with col2:
            if st.button("✏️", key=f"rename_{chat_id}"):
                st.session_state.current_chat = chat_id
                st.session_state.rename_mode = True

    if st.session_state.rename_mode and st.session_state.current_chat:
        new_name = st.text_input("Rename Chat")

        if st.button("Save Name"):
            st.session_state.chats[st.session_state.current_chat]["title"] = new_name
            st.session_state.rename_mode = False


# ---------------- MAIN ----------------
st.title("🤖 Multimodal AI Assistant")

if st.session_state.current_chat is None:
    st.info("👈 Start a new chat")
    st.stop()

chat_id = st.session_state.current_chat
chat_data = st.session_state.chats[chat_id]


# ---------------- CHAT ----------------
for msg in chat_data["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg.get("image"):
            st.image(msg["image"], width=250)


# ================= INPUT AREA =================
st.markdown("---")

col1, col2 = st.columns([1, 10])

with col1:
    if st.button("➕"):
        st.session_state.show_menu = not st.session_state.show_menu

with col2:
    user_text = st.chat_input("Type your message...")


# ---------------- ACTION PANEL ----------------
final_input = None
image_path = None

if st.session_state.show_menu:

    st.markdown("### Choose Input")

    colA, colB = st.columns(2)

    # IMAGE
    with colA:
        uploaded = st.file_uploader(
            "Upload Image",
            type=["png", "jpg", "jpeg"],
            key=f"img_{chat_id}"
        )

        question = st.text_input(
            "Ask about image",
            key=f"img_q_{chat_id}"
        )

        if uploaded:
            st.image(uploaded, width=150)

        if st.button("Send Image", key=f"send_img_{chat_id}"):
            if uploaded and question:
                image_path = save_uploaded_file(uploaded)
                final_input = question
            else:
                st.warning("Upload image + enter question")

    # VOICE 
    with colB:
        audio = st.audio_input(
            "Speak your query",
            key=f"voice_{chat_id}"
        )

        if audio is not None:

            audio_bytes = audio.getbuffer()
            audio_hash = hashlib.md5(audio_bytes).hexdigest()

            # 🔥 process only new audio
            if audio_hash != st.session_state.last_audio_hash:

                st.session_state.last_audio_hash = audio_hash

                audio_path = f"assets/temp/audio_{chat_id}.wav"

                with open(audio_path, "wb") as f:
                    f.write(audio_bytes)

                final_input = transcribe(audio_path)
                st.success(f"🎤 {final_input}")


# ---------------- TEXT INPUT ----------------
if user_text:
    final_input = user_text


# ---------------- PROCESS ----------------
if final_input:

    if len(chat_data["messages"]) == 0:
        chat_data["title"] = generate_chat_title(final_input)

    add_message(chat_data["messages"], "user", final_input, image_path)

    with st.spinner("Thinking..."):
        response = get_response(
            text=final_input,
            image_path=image_path,
            history=chat_data["messages"]
        )

    add_message(chat_data["messages"], "assistant", response)

    st.rerun()