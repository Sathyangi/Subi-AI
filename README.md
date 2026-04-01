# ✦ Subi AI — Your Personal AI Chatbot

A beautifully designed, fully interactive AI chatbot built with **Python**, **Streamlit**, and **Groq**. Features a stunning dark/light mode UI, real-time chat, and a friendly AI assistant named Subi.

<img width="1761" height="778" alt="Subiai" src="https://github.com/user-attachments/assets/7bdcd815-2675-449a-8cc4-1f3f5f5d4b84" />



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
| <img width="1756" height="777" alt="dark" src="https://github.com/user-attachments/assets/ea36a82f-519d-4b64-a701-e60526b913a9" />

| <img width="1748" height="776" alt="light" src="https://github.com/user-attachments/assets/c0496295-ebc3-439a-be68-b771a1e67230" />
|

> **See also:** 
<img width="1740" height="770" alt="con" src="https://github.com/user-attachments/assets/68ed64c7-2cdf-496d-91ca-0cc0c4b181af" />


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
git clone  https://github.com/Sathyangi/Subi-AI.git
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

##  Credits

- **Groq** — blazing fast free AI inference
- **Streamlit** — effortless Python web apps
- **Meta Llama 3.3** — the AI model powering Subi

---

*Built with ❤️ by Subodha*
