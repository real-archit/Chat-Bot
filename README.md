# 🧠 Chatbox – Real-Time Gemini AI Chatbot

Chatbox is a real-time chatbot web app built with **Google’s Gemini Pro (Flash 2.0)** model and **Streamlit**. It allows users to have seamless, intelligent conversations with the Gemini AI, directly in the browser.

---

## 🚀 Features

- 🤖 Powered by Google Gemini 2.0 Flash model
- 💬 Real-time question answering & conversation
- 📜 Persistent chat history across user sessions
- ⚠️ Input validation & error handling
- ⚡ Lightweight, responsive UI with Streamlit

---

## 🛠️ Tech Stack

- **Python 3.12+**
- **Streamlit** for the web interface
- **Google Generative AI SDK (gemini)**

---


## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/real-archit/chatbox.git
cd chatbox
2. Create & Activate Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python3 -m venv gemini-env
source gemini-env/bin/activate  # On Windows: gemini-env\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your Gemini API Key
Replace the placeholder API key in app.py:

python
Copy
Edit
API_KEY = "YOUR_GEMINI_API_KEY"
You can get your Gemini API key from: https://makersuite.google.com/app/apikey

🧪 Run the App
bash
Copy
Edit
streamlit run app.py
Open the app in your browser at http://localhost:8501

📁 File Structure
bash
Copy
Edit
chatbox/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Required Python packages
└── README.md            # Project description
✅ Requirements
Python 3.12+

Internet connection (to access Gemini API)

📜 License
This project is open-source and free to use under the MIT License.

🤝 Contributing
Pull requests, issues, and suggestions are welcome! Feel free to fork and enhance Chatbox.

🌐 Credits
Built by Archit Tiwari

Powered by Google Generative AI

UI with Streamlit

yaml
Copy
Edit

---

### 📦 Sample `requirements.txt`

Also include this in your repo:

streamlit
google-generativeai

yaml
Copy
Edit

---
