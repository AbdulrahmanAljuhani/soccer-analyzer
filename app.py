import streamlit as st
import requests

# --- Config ---
API_KEY = "your_together_api_key_here"  # Replace this!
MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# --- Sample tracking data ---
tracking_data = {
    "frame_15.jpg": {"position": [197, 125]},
    "frame_30.jpg": {"position": [315, 140]},
    "frame_45.jpg": {"position": [340, 145]},
    "frame_60.jpg": {"position": [360, 150]},
    "frame_75.jpg": {"position": [375, 153]},
    "frame_90.jpg": {"position": [400, 160]},
}

# --- Prompt builder ---
def build_prompt(question, tracking_data):
    intro = (
        "You are an AI soccer analyst. You are analyzing player movement across multiple video frames from a soccer match.\n"
        "The following are the tracked positions of one player across time:\n\n"
    )
    frames = "".join([f"- {frame}: Position {info['position']}\n" for frame, info in tracking_data.items()])
    return intro + frames + f"\n\nNow, based on these positions, answer the following:\n{question}"

# --- API Caller ---
def ask_ai(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "prompt": prompt[-2000:],
        "max_tokens": 300,
        "temperature": 0.7,
        "top_p": 0.9,
    }

    response = requests.post("https://api.together.xyz/v1/completions", json=data, headers=headers)

    try:
        result = response.json()
        st.json(result)  # 🔍 Show raw response (optional)
        return result["choices"][0]["text"].strip()
    except Exception as e:
        st.error("⚠️ AI failed to respond. Check your model/API key or logs.")
        st.code(response.text, language='json')  # Show full error response
        return ""

# --- UI ---
st.title("⚽ AI Soccer Player Analyzer")
question = st.text_input("Ask a question about this player's movement:")

if st.button("Analyze"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        prompt = build_prompt(question, tracking_data)
        with st.spinner("Thinking..."):
            answer = ask_ai(prompt)
            if answer:
                st.success("✅ AI Response:")
                st.write(answer)
