# ✦ Subi AI — Your Personal AI Chatbot

A beautifully designed, fully interactive AI chatbot built with **Python**, **Streamlit**, and **Groq**. Features a stunning dark/light mode UI, real-time chat, and a friendly AI assistant named Subi.

<img width="1761" height="778" alt="Subiai" src="https://github.com/user-attachments/assets/10a845c5-cfcb-489b-8521-78c690b144ac" />


---

## ✨ Features

- 🌙☀️ **Full Dark / Light mode** — toggle switches the entire UI
- 💬 **Real-time AI chat** — powered by Llama 3.3 70B via Groq (free!)
- 🎨 **Custom UI** — gradient backgrounds, styled chat bubbles, animated pulse indicator
- 📊 **Live stats** — message count and character count in the sidebar
- 🗑️ **Clear chat** — reset the conversation anytime
- 🔒 **Secure** — API key stored in `.env`, never hardcoded

---

## 📸 Screenshots

| Dark Mode | Light Mode |
|-----------|------------|
| <img width="1756" height="777" alt="dark" src="https://github.com/user-attachments/assets/4ed0c01d-1670-45d1-9fdd-83bf165a3344" />
 |<img width="1748" height="776" alt="light" src="https://github.com/user-attachments/assets/ef583a4c-bf6a-4575-8909-3758c3818f8f" />
 |

> **See also:** 
<img width="1740" height="770" alt="con" src="https://github.com/user-attachments/assets/9208e03e-06aa-479a-bfec-22a5a3c5bad5" />

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| Streamlit | Web UI framework |
| Groq API | Free AI inference (Llama 3.3 70B) |
| python-dotenv | Secure API key management |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/subi-ai.git
cd subi-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit groq python-dotenv
```

### 4. Get a free Groq API key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for free
3. Click **API Keys → Create API Key**
4. Copy the key (starts with `gsk_...`)

### 5. Create your `.env` file

```bash
GROQ_API_KEY=gsk_your_key_here
```

### 6. Run the app

```bash
streamlit run app.py
```

Your chatbot opens at **http://localhost:8501** 🎉

---

## 📁 Project Structure

```
subi-ai/
├── app.py           ← Main chatbot application
├── .env             ← Your API key (never commit this!)
├── .gitignore       ← Protects your secrets
├── README.md        ← You are here
└── screenshots/     ← UI screenshots
    ├── dark-mode.png
    ├── light-mode.png
    └── chat-example.png
```

---

## ⚙️ Customization

### Change the bot's personality
Edit the `SYSTEM_PROMPT` in `app.py`:
```python
SYSTEM_PROMPT = """You are Subi, a helpful AI assistant.
Add any personality traits you like here!"""
```

### Change the AI model
Swap the model name in `app.py`:
```python
model="llama-3.3-70b-versatile"   # default — smart and fast
model="mixtral-8x7b-32768"         # alternative option
```

---

## 🔒 Security Note

Never commit your `.env` file. This project's `.gitignore` already excludes it. Your API key stays safe on your machine only.

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 🙏 Credits

- **Groq** — blazing fast free AI inference
- **Streamlit** — effortless Python web apps
- **Meta Llama 3.3** — the AI model powering Subi

---

*Built with ❤️ by Subodha*
