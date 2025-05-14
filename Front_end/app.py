import streamlit as st
import requests

st.set_page_config(page_title="💪 AI Muscle Coach", layout="wide")

# --------------------
# 🎨 Styling
# --------------------
st.markdown("""
    <style>
    body {
        background-color: #111827;
        color: #f9fafb;
    }

    .big-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #f9fafb;
    }

    .hero {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }

    .response-box {
        background-color: #1f2937;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.5);
        animation: fadein 1s;
    }

    .question {
        font-size: 1.2rem;
        font-weight: 600;
        color: #f9fafb;
    }

    .answer {
        font-size: 1rem;
        color: #f9fafb;
        line-height: 1.6;
    }

    .input-highlight {
        background: linear-gradient(to right, #38bdf8, #6366f1);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem;
    }

    @keyframes fadein {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    @media (max-width: 768px) {
        .big-title { font-size: 2rem; }
        .hero { padding: 1rem; }
    }
    </style>
""", unsafe_allow_html=True)

# --------------------
# 🏋️‍♂️ Hero Section
# --------------------
st.markdown("""
<div class="hero">
    <div class="big-title">💪 AI Muscle Coach</div>
    <p style="color:#f1f5f9">Ask about muscle training, form, or growth — or choose a preset below.</p>
</div>
""", unsafe_allow_html=True)

# --------------------
# 💥 Sidebar Muscle Select
# --------------------
st.sidebar.header("🎯 Target a Muscle Group")
muscle_options = [
    None,
    "Best bicep exercises",
    "Effective tricep routine",
    "How to hit rear delts",
    "Squat form for glutes",
    "Chest hypertrophy tips",
    "Calf muscle building"
]
selected_muscle = st.sidebar.radio("Choose a focus area:", muscle_options)

# --------------------
# ✍️ User Input Area
# --------------------
st.markdown("### 📝 <span class='input-highlight'>Ask Your Own Question</span>", unsafe_allow_html=True)
free_text = st.text_input("", placeholder="Type your muscle query here...")

# --------------------
# 🧠 Compose Final Query
# --------------------
final_query = free_text or selected_muscle

# --------------------
# 🔄 Send to Backend
# --------------------
if final_query:
    st.markdown(f"<div class='question'>🔍 Asking: <strong>{final_query}</strong></div>", unsafe_allow_html=True)

    with st.spinner("💡 Thinking..."):
        try:
            response = requests.get("http://localhost:8000/ask", params={"query": final_query})
            if response.status_code == 200:
                answer = response.json().get("response", "")
                st.markdown(f"<div class='response-box'><div class='answer'>{answer}</div></div>", unsafe_allow_html=True)
            else:
                st.error("🚫 Backend returned an error.")
        except Exception as e:
            st.error(f"❌ Could not connect to backend: {e}")
