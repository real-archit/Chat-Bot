import google.generativeai as genai
import streamlit as st

# Configure your Gemini API key
API_KEY = "AIzaSyCH71RnSBukqI-1CWXwhUuFhODzhnLK9e4"
genai.configure(api_key=API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit app title and description
st.title("🧠 Chat-Box - AI Chatbot")
st.markdown("Talk to AI in real-time!")

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("You:")

if user_input:
    # Store and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get Gemini response
    try:
        response = st.session_state.chat.send_message(user_input)
        assistant_reply = response.text

        # Store and display bot response
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

    except ValueError:
        st.error("⚠️ Please enter a valid message.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")


