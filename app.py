import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="Subi AI",
    page_icon="✦",
    layout="centered"
)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True
if "messages" not in st.session_state:
    st.session_state.messages = []
if "total_chars" not in st.session_state:
    st.session_state.total_chars = 0

dark = st.session_state.dark_mode

# --- Theme variables ---
if dark:
    bg_main       = "#080810"
    bg_gradient   = "radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99,60,255,0.25) 0%, transparent 60%), radial-gradient(ellipse 60% 40% at 80% 80%, rgba(0,210,180,0.12) 0%, transparent 50%), #080810"
    sidebar_bg    = "rgba(12,12,22,0.97)"
    sidebar_border= "rgba(255,255,255,0.06)"
    text_primary  = "#e2e8f0"
    text_muted    = "#94a3b8"
    text_faint    = "rgba(255,255,255,0.25)"
    input_bg      = "rgba(255,255,255,0.05)"
    input_border  = "rgba(255,255,255,0.12)"
    user_bubble_bg= "rgba(99,60,255,0.15)"
    user_bubble_bd= "rgba(99,60,255,0.3)"
    ai_bubble_bg  = "rgba(255,255,255,0.04)"
    ai_bubble_bd  = "rgba(255,255,255,0.08)"
    stat_bg       = "rgba(255,255,255,0.04)"
    stat_border   = "rgba(255,255,255,0.08)"
    divider       = "rgba(255,255,255,0.06)"
    btn_bg        = "rgba(255,255,255,0.05)"
    btn_border    = "rgba(255,255,255,0.1)"
    btn_color     = "rgba(255,255,255,0.6)"
    header_border = "rgba(255,255,255,0.08)"
    logo_gradient = "linear-gradient(135deg, #a78bfa 0%, #34d399 100%)"
    toggle_icon   = "☀️"
    toggle_label  = "Light mode"
else:
    bg_main       = "#f4f3ff"
    bg_gradient   = "radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99,60,255,0.1) 0%, transparent 60%), radial-gradient(ellipse 60% 40% at 80% 80%, rgba(0,180,150,0.08) 0%, transparent 50%), #f4f3ff"
    sidebar_bg    = "rgba(255,255,255,0.97)"
    sidebar_border= "rgba(99,60,255,0.15)"
    text_primary  = "#1e1b4b"
    text_muted    = "#4b5563"
    text_faint    = "rgba(0,0,0,0.35)"
    input_bg      = "rgba(255,255,255,0.9)"
    input_border  = "rgba(99,60,255,0.25)"
    user_bubble_bg= "rgba(99,60,255,0.1)"
    user_bubble_bd= "rgba(99,60,255,0.25)"
    ai_bubble_bg  = "rgba(255,255,255,0.85)"
    ai_bubble_bd  = "rgba(99,60,255,0.12)"
    stat_bg       = "rgba(99,60,255,0.06)"
    stat_border   = "rgba(99,60,255,0.12)"
    divider       = "rgba(99,60,255,0.1)"
    btn_bg        = "rgba(99,60,255,0.08)"
    btn_border    = "rgba(99,60,255,0.2)"
    btn_color      = "#4c1d95"
    header_border = "rgba(99,60,255,0.1)"
    logo_gradient = "linear-gradient(135deg, #6d28d9 0%, #0f9b6e 100%)"
    toggle_icon   = "🌙"
    toggle_label  = "Dark mode"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section.main,
.main .block-container {{
    background: {bg_main} !important;
    font-family: 'DM Sans', sans-serif !important;
}}

[data-testid="stAppViewContainer"] {{
    background: {bg_gradient} !important;
    min-height: 100vh;
}}

[data-testid="stHeader"] {{
    background: transparent !important;
    backdrop-filter: none !important;
}}

[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {{
    background: {sidebar_bg} !important;
    border-right: 1px solid {sidebar_border} !important;
    backdrop-filter: blur(20px);
}}

[data-testid="stChatMessage"] {{
    background: transparent !important;
    border: none !important;
    padding: 0.4rem 0 !important;
}}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stMarkdownContainer"] {{
    background: {user_bubble_bg} !important;
    border: 1px solid {user_bubble_bd} !important;
    border-radius: 18px 18px 4px 18px !important;
    padding: 12px 16px !important;
    color: {text_primary} !important;
}}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) [data-testid="stMarkdownContainer"] {{
    background: {ai_bubble_bg} !important;
    border: 1px solid {ai_bubble_bd} !important;
    border-radius: 18px 18px 18px 4px !important;
    padding: 12px 16px !important;
    color: {text_muted} !important;
}}

[data-testid="stChatMessageAvatarUser"] {{
    background: linear-gradient(135deg, #6b3cf5, #a78bfa) !important;
    border: none !important;
}}
[data-testid="stChatMessageAvatarAssistant"] {{
    background: linear-gradient(135deg, #0f9b6e, #34d399) !important;
    border: none !important;
}}

[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] {{
    background: {input_bg} !important;
    border: 1px solid {input_border} !important;
    border-radius: 16px !important;
    color: {text_primary} !important;
    font-family: 'DM Sans', sans-serif !important;
}}
[data-testid="stChatInput"]:focus-within {{
    border-color: rgba(99,60,255,0.6) !important;
    box-shadow: 0 0 0 3px rgba(99,60,255,0.15) !important;
}}
[data-testid="stChatInput"] textarea::placeholder {{
    color: {text_faint} !important;
}}

.stButton > button {{
    background: {btn_bg} !important;
    border: 1px solid {btn_border} !important;
    color: {btn_color} !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.8rem !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}}
.stButton > button:hover {{
    background: rgba(99,60,255,0.2) !important;
    border-color: rgba(99,60,255,0.4) !important;
    color: {'white' if dark else '#3b0764'} !important;
}}

p, li, [data-testid="stMarkdownContainer"] p {{
    color: {text_muted} !important;
}}

.subi-header {{
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}}
.subi-logo {{
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    background: {logo_gradient};
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
    line-height: 1;
}}
.subi-tagline {{
    font-size: 0.85rem;
    color: {text_faint};
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-top: 6px;
    font-weight: 300;
}}
.subi-pulse {{
    width: 8px; height: 8px;
    background: #34d399;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    animation: pulse 2s infinite;
}}
@keyframes pulse {{
    0%, 100% {{ opacity: 1; box-shadow: 0 0 0 0 rgba(52,211,153,0.4); }}
    50% {{ opacity: 0.7; box-shadow: 0 0 0 6px rgba(52,211,153,0); }}
}}
.sidebar-title {{
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: {text_primary};
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid {header_border};
}}
.stat-box {{
    background: {stat_bg};
    border: 1px solid {stat_border};
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 8px;
}}
.stat-label {{
    font-size: 0.7rem;
    color: {text_faint};
    text-transform: uppercase;
    letter-spacing: 0.1em;
}}
.stat-value {{
    font-size: 1.2rem;
    font-weight: 600;
    color: {text_primary};
    font-family: 'Syne', sans-serif;
}}
.model-badge {{
    display: inline-block;
    background: rgba(52,211,153,0.15);
    border: 1px solid rgba(52,211,153,0.3);
    color: #0f9b6e;
    font-size: 0.7rem;
    padding: 3px 10px;
    border-radius: 99px;
    font-weight: 500;
    letter-spacing: 0.05em;
}}
.divider {{
    height: 1px;
    background: {divider};
    margin: 1rem 0;
}}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="subi-header">
    <div class="subi-logo">✦ Subi</div>
    <div class="subi-tagline"><span class="subi-pulse"></span>AI Assistant · Online</div>
</div>
""", unsafe_allow_html=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are Subi, a brilliant and witty AI assistant.
You are sharp, concise, and thoughtful. You communicate clearly,
use examples when helpful, and have a warm personality.
Keep responses focused and avoid unnecessary filler."""

# Sidebar
with st.sidebar:
    st.markdown(f'<div class="sidebar-title">✦ Subi Control Panel</div>', unsafe_allow_html=True)

    # Dark/Light toggle
    if st.button(f"{toggle_icon}  {toggle_label}"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    st.markdown(f'<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="stat-box"><div class="stat-label">Messages</div><div class="stat-value">{len(st.session_state.messages)}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="stat-box"><div class="stat-label">Characters</div><div class="stat-value">{st.session_state.total_chars}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown(f'**Model**')
    st.markdown('<span class="model-badge">llama-3.3-70b-versatile</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="divider"></div>', unsafe_allow_html=True)

    if st.button("🗑️  Clear conversation"):
        st.session_state.messages = []
        st.session_state.total_chars = 0
        st.rerun()

    st.markdown(f'<div style="margin-top:2rem; font-size:0.7rem; color:{text_faint}; text-align:center;">Powered by Groq · Free tier</div>', unsafe_allow_html=True)

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
if prompt := st.chat_input("Ask Subi anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.total_chars += len(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner(""):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.total_chars += len(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()