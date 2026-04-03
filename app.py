import streamlit as st
import pickle
import time

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def check_spam(message):
    msg_vec = vectorizer.transform([message])
    prediction = model.predict(msg_vec)
    prob = model.predict_proba(msg_vec)
    confidence = max(prob[0]) * 100
    return prediction[0], confidence

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="SpamShield AI", page_icon="🛡️", layout="centered")

# =========================
# 🔥 CUSTOM CSS (NO WHITE BG + ATTRACTIVE UI)
# =========================
st.markdown("""
<style>

/* REMOVE WHITE BACKGROUND */
html, body, [class*="css"]  {
    background: transparent !important;
}

/* FULL BACKGROUND */
.stApp {
    background: linear-gradient(-45deg, #0f2027, #1a2980, #26d0ce, #1e3c72);
    background-size: 400% 400%;
    animation: gradientMove 10s ease infinite;
}

/* ANIMATION */
@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* GLOW CIRCLES */
.stApp::before {
    content: "";
    position: fixed;
    width: 400px;
    height: 400px;
    background: rgba(0, 255, 255, 0.15);
    border-radius: 50%;
    top: 10%;
    left: 10%;
    filter: blur(120px);
}

.stApp::after {
    content: "";
    position: fixed;
    width: 300px;
    height: 300px;
    background: rgba(255, 0, 150, 0.15);
    border-radius: 50%;
    bottom: 10%;
    right: 10%;
    filter: blur(120px);
}

/* MAIN CARD */
.main-box {
    background: rgba(0, 0, 0, 0.6);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 0px 25px rgba(0,255,255,0.2);
}

/* TITLE */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #00f5d4;
}

/* SUBTEXT */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 20px;
}

/* TEXT AREA */
textarea {
    background-color: rgba(0,0,0,0.7) !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid #00f5d4 !important;
}

/* BUTTON */
.stButton button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #00f5d4, #00bbf9);
    color: black;
    font-weight: bold;
    font-size: 16px;
}

.stButton button:hover {
    transform: scale(1.05);
}

/* RESULT */
.result-box {
    text-align:center;
    font-size: 20px;
    font-weight: bold;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# UI START
# =========================

st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown('<div class="title">🛡️ SpamShield AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Message Analyzer</div>', unsafe_allow_html=True)

# INPUT
user_input = st.text_area("✉️ Enter Message", height=150)

# BUTTON
if st.button("🚀 Scan Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        with st.spinner("Analyzing..."):
            time.sleep(1.5)

        result, confidence = check_spam(user_input)

        if result == 1:
            st.markdown(f'<div class="result-box" style="color:#ff4d6d;">🚨 SPAM ({confidence:.2f}%)</div>', unsafe_allow_html=True)
            st.progress(int(confidence))
            st.markdown("🔴 Risk Level: High")
        else:
            st.markdown(f'<div class="result-box" style="color:#00f5d4;">✅ SAFE ({confidence:.2f}%)</div>', unsafe_allow_html=True)
            st.progress(int(confidence))
            st.markdown("🟢 Risk Level: Low")

st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>⚡ AI Message Scanner</p>", unsafe_allow_html=True)